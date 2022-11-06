from hashlib import new
import pandas as pd
import numpy as np

# Prepare orders data


def prepare_orders_data(orders):
    '''Prepare orders data
    
    Input:
    orders: a dataframe with customers orders
    
    Output:
    orders_by_customer: pandas dataframe with orders data grouped by customer_id   
    '''
    orders = pd.read_csv(orders_path)

    # Merge values in tshirt_category
    orders['tshirt_category'] = orders['tshirt_category'].replace(['Bl Tshirt F'], 'Black T-Shirt F')
    orders['tshirt_category'] = orders['tshirt_category'].replace(['Bl Tshirt M'], 'Black T-Shirt M')
    orders['tshirt_category'] = orders['tshirt_category'].replace(['Wh Tshirt M'], 'White T-Shirt M')
    orders['tshirt_category'] = orders['tshirt_category'].replace(['Wh Tshirt F'], 'White T-Shirt F')

    # Parse date columns as datetime
    orders['order_date'] = pd.to_datetime(orders['order_date'])

    # Create total_price column
    orders['total'] = orders['tshirt_quantity'] * orders['tshirt_price']

    # remove tshirt_price and tshirt_quantity
    orders = orders.drop(['tshirt_price', 'tshirt_quantity'], axis=1)

    # group orders by customer_id with min order_date total sum and avg pages_visited and count

    orders_by_customer = orders.groupby(['customer_id']).agg({'order_date': 'min', 'total': 'sum', 'pages_visited': 'mean', 'order_id': 'count'})

    # save orders_grouped to csv
    return orders_by_customer



#================= Join orders and customers  ====================


def prepare_customers(orders_by_customer, customers):
    '''Prepare customers data
    
    Input:
    orders_by_customer: a dataframe with customers orders grouped by customer_id
    customers: pandas dataframe with raw customers data
    
    Output:
    customers_prepared: pandas dataframe with key customers features, but witout high_revenue label
    
    '''

    # inner join customers and orders_by_customer by customer_id and customerID
    customers_prepared = pd.merge(customers, orders_by_customer, left_on='customerID', right_on='customer_id', how='inner')

    # parse date columns as datetime
    customers_prepared['order_date'] = pd.to_datetime(customers_prepared['order_date'])

    # change value "1993/2/29" to "1993/2/28" in birthdate
    customers_prepared['birthdate'] = customers_prepared['birthdate'].replace(['1993/2/29'], '1993/2/28')
    customers_prepared['birthdate'] = customers_prepared['birthdate'].replace(['1947/2/29'], '1947/2/28')   
    customers_prepared['birthdate'] = customers_prepared['birthdate'].replace(['1965/2/29'], '1965/2/28')   

    customers_prepared['birthdate'] = pd.to_datetime(customers_prepared['birthdate'])

    # Create age_firt_order column as order_date - birthdate in years
    customers_prepared['age_first_order'] = (customers_prepared['order_date'] - customers_prepared['birthdate']).dt.days / 365

    # Remove age_first_order outliers
    customers_prepared = customers_prepared[customers_prepared['age_first_order'] < 100]


    # extract browser from user_agent
    from user_agents import parse
    u1 = customers_prepared.head(1)['user_agent'].values[0]
    user_agent = parse(u1)
    user_agent.browser.family
    user_agent.os.family

    # parse user agent from user_agent
    def parse_user_agent(user_agent):
        user_agent = parse(user_agent)
        return user_agent.browser.family, user_agent.os.family

    # apply parse_user_agent to user_agent
    customers_prepared[['browser', 'os']] = customers_prepared['user_agent'].apply(parse_user_agent).apply(pd.Series)

    # remove birthdate, order_date, order_id, ip_address
    customers_prepared = customers_prepared.drop(['birthdate', 'order_date', 'order_id', 'ip_address', 'user_agent', 'Unnamed: 0'], axis=1)

    return customers_prepared


#==============  Label the dataset =================

def label_customers(customers_prepared):
    '''Add high_revenue label to each customer
    
    Input:
    customers_prepared: pandas dataframe with key customers features
    
    Output:
    customers_labeled: pandas dataframe with high_revenue label = TRUE for customers with total > 300 and FALSE otherwise
    '''
    
    # create high_revenue column
    customers_prepared['high_revenue'] = np.where(customers_prepared['total'] > 300, "True", "False")

    # create customers_labeled from customers_prepared without a total and customer_ID colums
    customers_labeled = customers_prepared.drop(['total'], axis=1)
    
    return customers_labeled


# === main code ===

# artiafacts paths
orders_path = 'data/01_raw/orders.csv'
orders_by_customer_path = 'data/02_transformed/orders_by_customers.csv'
customers_path = 'data/01_raw/customers.csv'
customers_prepared_path = 'data/03_prepared/customers_prepared.csv'
customers_labeled_path = 'data/03_prepared/customers_labeled.csv'

# dataframes
orders = pd.read_csv(orders_path)

orders_by_customer = prepare_orders_data(orders)
orders_by_customer.to_csv(orders_by_customer_path)

customers = pd.read_csv(customers_path)

customers_prepared = prepare_customers(orders_by_customer, customers)
customers_prepared.to_csv(customers_prepared_path, index=False)

customers_labeled = label_customers(customers_prepared)
customers_labeled.to_csv(customers_labeled_path, index=False)