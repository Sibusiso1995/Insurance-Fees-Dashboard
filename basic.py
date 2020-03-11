import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go 
import pandas as pd 
import plotly.offline as pyo

insure = pd.read_csv('insurance.csv')

app = dash.Dash()

app.layout = html.Div([
                dcc.Graph(id= 'Scatter',
                        figure={
                            'data':[go.Scatter(
                                x=insure['age'],
                                y=insure['charges'],
                                mode = 'markers'
                            )],
                            'layout': go.Layout(title='Age vs Charges',
                            xaxis={'title':'age'},
                            yaxis={'title':'charges'},
                            hovermode='closest')

                        }
                ),
                #chart 2
                html.Div([
                dcc.Graph(id= 'Box',
                        figure={
                            'data':[go.Box(
                                x=insure['sex'],
                                y=insure['bmi'],
                        
                            )],
                            'layout': go.Layout(title='Age vs Bmi',
                            xaxis={'title':'Gender'},
                            yaxis={'title':'bmi'}
                            )
                        }
               ),
                 #chart 3
                html.Div([
                    dcc.Graph(id= 'Bar',
                        figure={
                            'data':[go.Bar(
                                x=insure['sex'],
                                y=insure['charges'],
                                barmode='group'
                        
                            )],
                            'layout':go.Layout(title='Gender Vs Charges',
                            xaxis={'title':'Gender'},
                            yaxis={'title':'Charges'}
                            )
                        
                        }

                    ),
                    #Chart 4
                    html.Div([
                        dcc.Graph(id='Histogram',
                            figure={
                                'data':[go.Histogram(
                                    x=insure['bmi']

                                )],
                                'layout':go.Layout(title='BMI Variance',
                                xaxis={'title':'BMI'},
                                yaxis={'title':'Count'} 
                                )
                            }

                        )
                    ])       
            
               ])
        ])
])


if __name__ == '__main__':
    app.run_server()
