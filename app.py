import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load the CSV data
data = pd.read_csv('projectds.csv')

# Perform basic analysis for different graphs
scatter_analysis = data.groupby('month')['tran_amount'].sum().reset_index()
to_3_month_analysis = data.groupby('month')['tran_amount'].mean().reset_index()
top_5_cust_analysis = data.groupby('customer_id')['tran_amount'].sum().nlargest(5).reset_index()
top_5_order_analysis = data.nlargest(5, 'tran_amount')
transaction_analysis = data.groupby('month')['tran_amount'].count().reset_index()

def generate_insights():
    scatter_insights = [
        f"Total transactions per month: {scatter_analysis['tran_amount'].sum()}",
        f"Month with the highest transactions: {scatter_analysis.loc[scatter_analysis['tran_amount'].idxmax()]['month']} ({scatter_analysis['tran_amount'].max()})"
    ]
    
    to_3_month_insights = [
        f"Average transaction amount per month: {to_3_month_analysis['tran_amount'].mean():.2f}",
        f"Month with the highest average transaction: {to_3_month_analysis.loc[to_3_month_analysis['tran_amount'].idxmax()]['month']} ({to_3_month_analysis['tran_amount'].max():.2f})"
    ]
    
    top_5_cust_insights = [
        f"Top 5 customers by transaction amount: {', '.join(top_5_cust_analysis['customer_id'].astype(str))}",
        f"Highest spending customer: {top_5_cust_analysis.iloc[0]['customer_id']} ({top_5_cust_analysis.iloc[0]['tran_amount']})"
    ]
    
    top_5_order_insights = [
        f"Top 5 orders by transaction amount: {', '.join(top_5_order_analysis['tran_amount'].astype(str))}",
        f"Highest transaction amount: {top_5_order_analysis.iloc[0]['tran_amount']}"
    ]
    
    transaction_insights = [
        f"Number of transactions per month: {transaction_analysis['tran_amount'].sum()}",
        f"Month with the highest number of transactions: {transaction_analysis.loc[transaction_analysis['tran_amount'].idxmax()]['month']} ({transaction_analysis['tran_amount'].max()})"
    ]
    
    return {
        'scatter': scatter_insights,
        'to_3_month': to_3_month_insights,
        'top_5_cust': top_5_cust_insights,
        'top_5_order': top_5_order_insights,
        'transaction': transaction_insights
    }

# Generate insights
insights = generate_insights()

# Function to create a collapsible card with a graph, a description, and insights
def create_card(card_id, title, src, insights):
    return dbc.Card([
        dbc.CardHeader(
            dbc.Button(
                title,
                id=f"{card_id}-button",
                color="link",
                n_clicks=0,
                style={'text-align': 'left', 'width': '100%'}
            )
        ),
        dbc.Collapse(
            dbc.CardBody([
                html.Iframe(
                    srcDoc=open(src, 'r', encoding='utf-8').read(),
                    style={'width': '100%', 'height': '400px'},
                    className='mb-2'
                ),
                html.Div(id=f"{card_id}-insights", children=[html.P(insight) for insight in insights], className='mb-2', style={'color': 'white'})
            ]),
            id=f"{card_id}-collapse",
            is_open=False
        )
    ], className='mb-4', style={'background-color': '#003b5c'})  # Persian Blue

# Create a layout for the dashboard
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Sales Performance Overview", className='text-center text-light'), width=12)
    ]),
    dbc.Row([
        dbc.Col(create_card("scatter", "Customer Activeness vs. Frequency Monetary", 'scatter_plot.html', insights['scatter']), width=12),
        dbc.Col(create_card("to_3_month", "To 3 Month Plot", 'to_3_month_plot.html', insights['to_3_month']), width=12),
        dbc.Col(create_card("top_5_cust", "Top 5 Customers Plot", 'top_5_cust_plot.html', insights['top_5_cust']), width=12),
        dbc.Col(create_card("top_5_order", "Top 5 Orders Plot", 'top_5_order_plot.html', insights['top_5_order']), width=12),
        dbc.Col(create_card("transaction", "Transaction Plot", 'transaction_plot.html', insights['transaction']), width=12)
    ])
], fluid=True, style={'background-color': '#003b5c', 'color': '#ffffff'})  # Persian Blue and text color

# Callback to toggle the collapse on card click
@app.callback(
    [Output(f"{card_id}-collapse", "is_open") for card_id in ["scatter", "to_3_month", "top_5_cust", "top_5_order", "transaction"]],
    [Input(f"{card_id}-button", "n_clicks") for card_id in ["scatter", "to_3_month", "top_5_cust", "top_5_order", "transaction"]],
    [State(f"{card_id}-collapse", "is_open") for card_id in ["scatter", "to_3_month", "top_5_cust", "top_5_order", "transaction"]],
)
def toggle_collapse(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        return [False] * 5
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    card_states = list(args[5:])
    index = ["scatter", "to_3_month", "top_5_cust", "top_5_order", "transaction"].index(button_id.split('-')[0])
    card_states[index] = not card_states[index]
    return card_states

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
