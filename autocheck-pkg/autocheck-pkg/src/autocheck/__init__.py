import altair as alt

def print_passed(msg):
    """Prints a message in green to indicate a passed test"""
    print("\033[92m[PASSED]\033[0m " + msg)

def print_info(msg):
    """Prints a message in blue to provide information"""
    print("\033[94m[INFO]\033[0m " + msg)

def print_failed(msg):
    """Prints a message in red to indicate a failed test"""
    print("\033[91m[FAILED]\033[0m " + msg)

def check_exercise1(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        if x_field == 'Body Mass (g)':
            print_passed("The x encoding channel used in your chart is correct.")
        else:
            print_failed("The x encoding channel used in your chart is incorrect. The x-axis should be encoded with 'Body Mass (g)'.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'Body Mass (g)'.")
        raise

def check_exercise2(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        if x_field == 'Body Mass (g)':
            print_passed("The x encoding channel used in your chart is correct.")
        else:
            print_failed("The x encoding channel used in your chart is incorrect. The x-axis should be encoded with 'Body Mass (g)'.")
        # Check if the x-axis scale zero is set to False
        x_scale = encoding.get('x', {}).get('scale', {})
        x_scale_zero = x_scale.get('zero')
        if x_scale_zero == False:
            print_passed("The x-axis scale zero is set to False.")
        else:
            print_failed("The x-axis scale zero is not set to False. The x-axis scale zero should be set to False to prevent misleading visualizations.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'Body Mass (g)'. The x-axis scale zero should be set to False to prevent misleading visualizations.")
        raise

def check_exercise3(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'Beak Length (mm)' and y_field == 'Beak Depth (mm)':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'Beak Length (mm)' and the y-axis should be encoded with 'Beak Depth (mm)'.")
        # Check if the axis scale zero is set to False
        x_scale = encoding.get('x', {}).get('scale', {})
        y_scale = encoding.get('y', {}).get('scale', {})
        x_scale_zero = x_scale.get('zero')
        y_scale_zero = y_scale.get('zero')
        if x_scale_zero == False and y_scale_zero == False:
            print_passed("The axis scale zero is set to False.")
        else:
            print_failed("The axis scale zero is not set to False. Both the x-axis scale zero and y-axis scale zero should be set to False to prevent misleading visualizations.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'Beak Length (mm)' and the y-axis should be encoded with 'Beak Depth (mm)'. Both the x-axis scale zero and y-axis scale zero should be set to False to prevent misleading visualizations.")
        raise

def check_exercise4(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'Beak Length (mm)' and y_field == 'Beak Depth (mm)':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'Beak Length (mm)' and the y-axis should be encoded with 'Beak Depth (mm)'.")
        # Check if the axis scale zero is set to False
        x_scale = encoding.get('x', {}).get('scale', {})
        y_scale = encoding.get('y', {}).get('scale', {})
        x_scale_zero = x_scale.get('zero')
        y_scale_zero = y_scale.get('zero')
        if x_scale_zero == False and y_scale_zero == False:
            print_passed("The axis scale zero is set to False.")
        else:
            print_failed("The axis scale zero is not set to False. Both the x-axis scale zero and y-axis scale zero should be set to False to prevent misleading visualizations.")
        # Check if the tooltip is included in the chart
        tooltip_field = encoding.get('tooltip', {}).get('field')
        if tooltip_field == 'Island':
            print_passed("The tooltip is included in the chart.")
        else:
            print_failed("The tooltip is not included in the chart. The tooltip should be encoded with 'Island' to provide additional information.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'Beak Length (mm)' and the y-axis should be encoded with 'Beak Depth (mm)'. Both the x-axis scale zero and y-axis scale zero should be set to False to prevent misleading visualizations. The tooltip should be encoded with 'Island' to provide additional information.")
        raise

def check_exercise5(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'Beak Length (mm)' and y_field == 'Beak Depth (mm)':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'Beak Length (mm)' and the y-axis should be encoded with 'Beak Depth (mm)'.")
        # Check if a tooltip is added
        mark_tooltip = None
        if isinstance(mark_type, dict):
            mark_tooltip = mark_type.get('tooltip')
        if mark_tooltip == True:
            print_passed("A tooltip is added to display the value of the `Beak Depth (mm)` and `Beak Length (mm)` for each point on hover.")
        else:
            print_failed("A tooltip is not added to display the value of the `Beak Depth (mm)` and `Beak Length (mm)` for each point on hover. You should use tooltip=True to enable the tooltip.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'Beak Length (mm)' and the y-axis should be encoded with 'Beak Depth (mm)'. A tooltip should be added to display the value of the `Beak Depth (mm)` and `Beak Length (mm)` for each point on hover.")
        raise

def check_exercise6(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'sepalLength' and y_field == 'sepalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'sepalLength' and the y-axis should be encoded with 'sepalWidth'.")
        # Check if the color encoding channel is added
        color_field = encoding.get('color', {}).get('field')
        if color_field == 'species':
            print_passed("The color of the points is encoded based on the 'species' column.")
        else:
            print_failed("The color of the points is not encoded based on the 'species' column. You should use `alt.Color('species')` to encode the color of the points based on the 'species' column.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'sepalLength' and the y-axis should be encoded with 'sepalWidth'. The color of the points should be encoded based on the 'species' column.")
        raise

def check_exercise7(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'petalLength' and y_field == 'petalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if the color encoding channel is added
        color_field = encoding.get('color', {}).get('field')
        if color_field == 'species':
            print_passed("The color of the points is encoded based on the 'species' column.")
            # Check if the color scale is specified correctly
            color_scale = encoding.get('color', {}).get('scale', {})
            domain_correct = color_scale.get('domain') == ['setosa', 'versicolor', 'virginica']
            range_correct = color_scale.get('range') == ['orangered', 'purple', 'seagreen']
            if domain_correct and range_correct:
                print_passed("The color scale is specified correctly.")
            else:
                print_failed("The color scale is not specified correctly. The domain of the color scale should be ['setosa', 'versicolor', 'virginica'] and the range of the color scale should be ['orangered', 'purple', 'seagreen'].")
        else:
            print_failed("The color of the points is not encoded based on the 'species' column. You should use `alt.Color('species', scale=alt.Scale(domain=['setosa', 'versicolor', 'virginica'], range=['orangered', 'purple', 'seagreen']))` to encode the color of the points based on the 'species' column.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'. The color of the points should be encoded based on the 'species' column using `alt.Color('species', scale=alt.Scale(domain=['setosa', 'versicolor', 'virginica'], range=['orangered', 'purple', 'seagreen']))`.")
        raise

def check_exercise8(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'petalLength' and y_field == 'petalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if the color encoding channel is added
        color_field = encoding.get('color', {}).get('field')
        if color_field == 'species':
            print_passed("The color of the points is encoded based on the 'species' column.")
        else:
            print_failed("The color of the points is not encoded based on the 'species' column. You should use `alt.Color('species')` to encode the color of the points based on the 'species' column.")
        # Check if the shape encoding channel is added
        shape_field = encoding.get('shape', {}).get('field')
        if shape_field == 'species':
            print_passed("The shape of the points is encoded based on the 'species' column.")
        else:
            print_failed("The shape of the points is not encoded based on the 'species' column. You should use `alt.Shape('species')` to encode the shape of the points based on the 'species' column.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'. The color of the points should be encoded based on the 'species' column. The shape of the points should be encoded based on the 'species' column.")
        raise

def check_exercise9(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'petalLength' and y_field == 'petalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if the axis scale zero is set to False
        x_scale = encoding.get('x', {}).get('scale', {})
        y_scale = encoding.get('y', {}).get('scale', {})
        x_scale_zero = x_scale.get('zero')
        y_scale_zero = y_scale.get('zero')
        if x_scale_zero == False and y_scale_zero == False:
            print_passed("The axis scale zero is set to False.")
        else:
            print_failed("The axis scale zero is not set to False. Both the x-axis scale zero and y-axis scale zero should be set to False to prevent misleading visualizations.")
        # Check if the column encoding channel is added
        column_field = encoding.get('column', {}).get('field')
        if column_field == 'species':
            print_passed("The 'species' column is encoded as separate columns in the plot.")
        else:
            print_failed("The 'species' column is not encoded as separate columns in the plot. You should use `alt.Column('species')` to encode the 'species' column as separate columns in the plot.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'. Both the x-axis scale zero and y-axis scale zero should be set to False to prevent misleading visualizations. The 'species' column should be encoded as separate columns in the plot.")
        raise

def check_exercise10(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'petalLength' and y_field == 'petalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if the axis scale zero is set to False
        x_scale = encoding.get('x', {}).get('scale', {})
        y_scale = encoding.get('y', {}).get('scale', {})
        x_scale_zero = x_scale.get('zero')
        y_scale_zero = y_scale.get('zero')
        if x_scale_zero == False and y_scale_zero == False:
            print_passed("The axis scale zero is set to False.")
        else:
            print_failed("The axis scale zero is not set to False. Both the x-axis scale zero and y-axis scale zero should be set to False to prevent misleading visualizations.")
        # Check if binning is used for the X-axis
        x_bin = encoding.get('x', {}).get('bin')
        if x_bin == True:
            print_passed("Binning is used for the X-axis.")
        else:
            print_failed("Binning is not used for the X-axis. You should use bin=True to bin the X-axis variable.")
        # Check if mean aggregation is used for the Y-axis
        y_aggregate = encoding.get('y', {}).get('aggregate')
        if y_aggregate == 'mean':
            print_passed("Mean aggregation is used for the Y-axis.")
        else:
            print_failed("Mean aggregation is not used for the Y-axis. You should use aggregate='mean' to aggregate the Y-axis variable.")
        # Check if tooltip aggregation is used for the petalLength variable
        tooltip_field = encoding.get('tooltip', {}).get('field')
        tooltip_aggregate = encoding.get('tooltip', {}).get('aggregate')
        if tooltip_field == 'petalLength' and tooltip_aggregate == 'mean':
            print_passed("Tooltip aggregation is used for the petalLength variable.")
        else:
            print_failed("Tooltip aggregation is not used for the petalLength variable. You should use tooltip=alt.Tooltip('petalLength', aggregate='mean') to aggregate the petalLength variable in the tooltip.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'. Both the x-axis scale zero and y-axis scale zero should be set to False to prevent misleading visualizations. Binning is used for the X-axis. Mean aggregation is used for the Y-axis. Tooltip aggregation is used for the petalLength variable.")
        raise

def check_exercise11(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_bar = mark_type.get('type') == 'bar'
        else:
            mark_is_bar = mark_type == 'bar'
        if mark_is_bar:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_bar() to create a bar chart.")
        # Check if the encoding channel for x-axis is correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        if x_field == 'petalLength':
            print_passed("The x-axis encoding channel used in your chart is correct.")
        else:
            print_failed("The x-axis encoding channel used in your chart is incorrect. The x-axis should be encoded with 'petalLength'.")
        # Check if the encoding channel for y-axis is correct
        y_aggregate = encoding.get('y', {}).get('aggregate')
        if y_aggregate == 'count':
            print_passed("The y-axis encoding channel used in your chart is correct.")
        else:
            print_failed("The y-axis encoding channel used in your chart is incorrect. The y-axis should be encoded with 'count()'.")
        # Check if the binning is correct for x-axis
        x_bin = encoding.get('x', {}).get('bin', {})
        x_maxbins = x_bin.get('maxbins') if isinstance(x_bin, dict) else None
        if x_maxbins == 10:
            print_passed("The binning used in your chart is correct.")
        else:
            print_failed("The binning used in your chart is incorrect. The x-axis should use `alt.Bin(maxbins=10)` to bin the `petalLength` values.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_bar() to create a bar chart. The x-axis should be encoded with 'petalLength', the y-axis should be encoded with 'count()', and the x-axis should use `alt.Bin(maxbins=10)` to bin the `petalLength` values.")
        raise

def check_exercise12(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_rect = mark_type.get('type') == 'rect'
        else:
            mark_is_rect = mark_type == 'rect'
        if mark_is_rect:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_rect() to create a heatmap.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'petalLength' and y_field == 'petalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if the binning is done correctly
        x_bin = encoding.get('x', {}).get('bin', {})
        y_bin = encoding.get('y', {}).get('bin', {})
        x_extent = x_bin.get('extent') if isinstance(x_bin, dict) else None
        x_step = x_bin.get('step') if isinstance(x_bin, dict) else None
        y_maxbins = y_bin.get('maxbins') if isinstance(y_bin, dict) else None
        if x_extent == [1.5, 7.5] and x_step == 0.5 and y_maxbins == 20:
            print_passed("The binning is done correctly.")
        else:
            print_failed("The binning is not done correctly. The x-axis should be binned using `bin=alt.Bin(extent=[1.5, 7.5], step=0.5)` and the y-axis should be binned using `bin=alt.Bin(maxbins=20)`.")
        # Check if the color encoding is correct
        color_aggregate = encoding.get('color', {}).get('aggregate')
        if color_aggregate == 'count':
            print_passed("The chart has a color encoding.")
        else:
            print_failed("The chart does not have a color encoding. You should use `alt.Color('count()')` to color the heatmap.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_rect() to create a heatmap. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'. The x-axis should be binned using `bin=alt.Bin(extent=[1.5, 7.5], step=0.5)` and the y-axis should be binned using `bin=alt.Bin(maxbins=20)`. The chart should have a color encoding using `alt.Color('count()')`.")
        raise

def check_exercise13(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_bar = mark_type.get('type') == 'bar'
        else:
            mark_is_bar = mark_type == 'bar'
        if mark_is_bar:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_bar() to create a bar chart.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_aggregate = encoding.get('x', {}).get('aggregate')
        y_field = encoding.get('y', {}).get('field')
        if x_aggregate == 'count' and y_field == 'species':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'count()' and the y-axis should be encoded with 'species'.")
        # Check if a tooltip is added
        tooltip_field = encoding.get('tooltip', {}).get('field')
        tooltip_aggregate = encoding.get('tooltip', {}).get('aggregate')
        if tooltip_field == 'petalWidth' and tooltip_aggregate == 'mean':
            print_passed("A tooltip is added to display the mean petal width for each species.")
        else:
            print_failed("A tooltip is not added to display the mean petal width for each species. You should use alt.Tooltip('petalWidth', aggregate='mean') to add a tooltip.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_bar() to create a bar chart. The x-axis should be encoded with 'count()' and the y-axis should be encoded with 'species'. A tooltip should be added to display the mean petal width for each species.")
        raise

def check_exercise14(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct
        mark_type = chart_dict.get('mark', {})
        if isinstance(mark_type, dict):
            mark_is_point = mark_type.get('type') == 'point'
        else:
            mark_is_point = mark_type == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct
        encoding = chart_dict.get('encoding', {})
        x_field = encoding.get('x', {}).get('field')
        y_field = encoding.get('y', {}).get('field')
        if x_field == 'petalLength' and y_field == 'petalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if the chart is filtered correctly
        transform = chart_dict.get('transform', [])
        filter_found = False
        for t in transform:
            if t.get('filter') == "datum.species === 'versicolor'":
                filter_found = True
                break
        if filter_found:
            print_passed("The chart is filtered to only show data points where the species is 'versicolor'.")
        else:
            print_failed("The chart is not filtered to only show data points where the species is 'versicolor'. You should use `transform_filter(\"datum.species === 'versicolor'\")` to filter the chart.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'. The chart should be filtered to only show data points where the species is 'versicolor'.")
        raise

def check_exercise15(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct (first layer)
        layer_0 = chart_dict.get('layer', [])[0] if chart_dict.get('layer') else {}
        mark_type_0 = layer_0.get('mark', {})
        if isinstance(mark_type_0, dict):
            mark_is_point = mark_type_0.get('type') == 'point'
        else:
            mark_is_point = mark_type_0 == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct (first layer)
        encoding_0 = layer_0.get('encoding', {})
        x_field = encoding_0.get('x', {}).get('field')
        y_field = encoding_0.get('y', {}).get('field')
        if x_field == 'petalLength' and y_field == 'petalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if a rule is added to show the mean of petalWidth (second layer)
        layer_1 = chart_dict.get('layer', [])[1] if len(chart_dict.get('layer', [])) > 1 else {}
        mark_type_1 = layer_1.get('mark', {})
        if isinstance(mark_type_1, dict):
            mark_is_rule = mark_type_1.get('type') == 'rule'
        else:
            mark_is_rule = mark_type_1 == 'rule'
        if mark_is_rule:
            print_passed("A rule is added to show the mean of `petalWidth`.")
        else:
            print_failed("A rule is not added to show the mean of `petalWidth`. You should use mark_rule() to create a rule.")
        # Check if the y-axis of the rule is correct
        encoding_1 = layer_1.get('encoding', {})
        y_field_rule = encoding_1.get('y', {}).get('field')
        y_aggregate_rule = encoding_1.get('y', {}).get('aggregate')
        if y_field_rule == 'petalWidth' and y_aggregate_rule == 'mean':
            print_passed("The y-axis of the rule shows the mean of `petalWidth`.")
        else:
            print_failed("The y-axis of the rule does not show the mean of `petalWidth`. You should use `mean(petalWidth)` to encode the y-axis of the rule.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'. A horizontal rule should be added to show the mean of `petalWidth`.")
        raise

def check_exercise16(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your chart is correct (first layer)
        layer_0 = chart_dict.get('layer', [])[0] if chart_dict.get('layer') else {}
        mark_type_0 = layer_0.get('mark', {})
        if isinstance(mark_type_0, dict):
            mark_is_point = mark_type_0.get('type') == 'point'
        else:
            mark_is_point = mark_type_0 == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your chart is correct.")
        else:
            print_failed("The type of mark used in your chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your chart are correct (first layer)
        encoding_0 = layer_0.get('encoding', {})
        x_field = encoding_0.get('x', {}).get('field')
        y_field = encoding_0.get('y', {}).get('field')
        if x_field == 'petalLength' and y_field == 'petalWidth':
            print_passed("The encoding channels used in your chart are correct.")
        else:
            print_failed("The encoding channels used in your chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if the horizontal line is added (second layer)
        layer_1 = chart_dict.get('layer', [])[1] if len(chart_dict.get('layer', [])) > 1 else {}
        mark_type_1 = layer_1.get('mark', {})
        if isinstance(mark_type_1, dict):
            mark_is_rule = mark_type_1.get('type') == 'rule'
        else:
            mark_is_rule = mark_type_1 == 'rule'
        if mark_is_rule:
            print_passed("A horizontal line is added on the plot at the average value of the `petalWidth` column for each species of the iris flower.")
        else:
            print_failed("A horizontal line is not added on the plot at the average value of the `petalWidth` column for each species of the iris flower. You should use mark_rule() to create a rule.")
        # Check if the chart is colored by species
        color_field_0 = encoding_0.get('color', {}).get('field')
        encoding_1 = layer_1.get('encoding', {})
        color_field_1 = encoding_1.get('color', {}).get('field')
        if color_field_0 == 'species' and color_field_1 == 'species':
            print_passed("Each point and the rule is colored by species.")
        else:
            print_failed("Each point and the rule is not colored by species. You should use alt.Color(\"species\") to color the chart by species.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'. A horizontal line should be added on the plot at the average value of the `petalWidth` column for each species of the iris flower using mark_rule(). The chart should be colored by species using alt.Color(\"species\").")
        raise

def check_exercise17(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if both plots are combined using the '|' operator
        hconcat_charts = chart_dict.get('hconcat', [])
        if len(hconcat_charts) == 2:
            print_passed("Both plots are combined using the '|' operator.")
        else:
            print_failed("Both plots are not combined using the '|' operator. You should use the '|' operator to combine the plots side by side.")
        # Check if the type of mark used in your first chart is correct
        chart_0 = hconcat_charts[0] if len(hconcat_charts) > 0 else {}
        mark_type_0 = chart_0.get('mark', {})
        if isinstance(mark_type_0, dict):
            mark_is_point = mark_type_0.get('type') == 'point'
        else:
            mark_is_point = mark_type_0 == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your first chart is correct.")
        else:
            print_failed("The type of mark used in your first chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the type of mark used in your second chart is correct
        chart_1 = hconcat_charts[1] if len(hconcat_charts) > 1 else {}
        mark_type_1 = chart_1.get('mark', {})
        if isinstance(mark_type_1, dict):
            mark_is_bar = mark_type_1.get('type') == 'bar'
        else:
            mark_is_bar = mark_type_1 == 'bar'
        if mark_is_bar:
            print_passed("The type of mark used in your second chart is correct.")
        else:
            print_failed("The type of mark used in your second chart is incorrect. You should use mark_bar() to create a bar chart.")
        # Check if the encoding channels used in your first chart are correct
        encoding_0 = chart_0.get('encoding', {})
        x_field_0 = encoding_0.get('x', {}).get('field')
        y_field_0 = encoding_0.get('y', {}).get('field')
        if x_field_0 == 'petalLength' and y_field_0 == 'petalWidth':
            print_passed("The encoding channels used in your first chart are correct.")
        else:
            print_failed("The encoding channels used in your first chart are incorrect. The x-axis should be encoded with 'petalLength' and the y-axis should be encoded with 'petalWidth'.")
        # Check if the encoding channels used in your second chart are correct
        encoding_1 = chart_1.get('encoding', {})
        x_field_1 = encoding_1.get('x', {}).get('field')
        y_aggregate_1 = encoding_1.get('y', {}).get('aggregate')
        if x_field_1 == 'petalWidth' and y_aggregate_1 == 'count':
            print_passed("The encoding channels used in your second chart are correct.")
        else:
            print_failed("The encoding channels used in your second chart are incorrect. The x-axis should be encoded with 'petalWidth' and the y-axis should be encoded with 'count()'.")
    except:
        print_failed("Your solution did not generate the expected chart. You should use mark_point() to create a scatter plot for the first chart and mark_bar() to create a bar chart for the second chart. The x-axis of the first chart should be encoded with 'petalLength' and the y-axis with 'petalWidth'. The x-axis of the second chart should be encoded with 'petalWidth' and the y-axis with 'count()'. Both plots should be combined using the '|' operator.")
        raise

def check_exercise18(solution):
    try:
        display(solution)
        chart_dict = solution.to_dict()
        # Check if the type of mark used in your scatter plot chart is correct
        hconcat_charts = chart_dict.get('hconcat', [])
        chart_0 = hconcat_charts[0] if len(hconcat_charts) > 0 else {}
        mark_type_0 = chart_0.get('mark', {})
        if isinstance(mark_type_0, dict):
            mark_is_point = mark_type_0.get('type') == 'point'
        else:
            mark_is_point = mark_type_0 == 'point'
        if mark_is_point:
            print_passed("The type of mark used in your scatter plot chart is correct.")
        else:
            print_failed("The type of mark used in your scatter plot chart is incorrect. You should use mark_point() to create a scatter plot.")
        # Check if the encoding channels used in your scatter plot chart are correct
        encoding_0 = chart_0.get('encoding', {})
        x_field_0 = encoding_0.get('x', {}).get('field')
        y_field_0 = encoding_0.get('y', {}).get('field')
        if x_field_0 == 'sepalLength' and y_field_0 == 'sepalWidth':
            print_passed("The encoding channels used in your scatter plot chart are correct.")
        else:
            print_failed("The encoding channels used in your scatter plot chart are incorrect. The x-axis should be encoded with 'sepalLength' and the y-axis should be encoded with 'sepalWidth'.")
        # Check if the type of mark used in your histogram chart is correct
        chart_1 = hconcat_charts[1] if len(hconcat_charts) > 1 else {}
        mark_type_1 = chart_1.get('mark', {})
        if isinstance(mark_type_1, dict):
            mark_is_bar = mark_type_1.get('type') == 'bar'
        else:
            mark_is_bar = mark_type_1 == 'bar'
        if mark_is_bar:
            print_passed("The type of mark used in your histogram chart is correct.")
        else:
            print_failed("The type of mark used in your histogram chart is incorrect. You should use mark_bar() to create a histogram.")
        # Check if the encoding channels used in your histogram chart are correct
        encoding_1 = chart_1.get('encoding', {})
        x_field_1 = encoding_1.get('x', {}).get('field')
        y_aggregate_1 = encoding_1.get('y', {}).get('aggregate')
        if x_field_1 == 'sepalWidth' and y_aggregate_1 == 'count':
            print_passed("The encoding channels used in your histogram chart are correct.")
        else:
            print_failed("The encoding channels used in your histogram chart are incorrect. The x-axis should be encoded with 'sepalWidth' and the y-axis should be aggregated by 'count'.")
        # Check if the selection interval has been added to the scatter plot
        params = chart_dict.get('params', [])
        has_interval_selection = False
        for param in params:
            if param.get('select', {}).get('type') == 'interval':
                has_interval_selection = True
                break
        if has_interval_selection:
            print_passed("The selection interval has been added to the scatter plot.")
        else:
            print_failed("The selection interval is not added to the scatter plot. You should use alt.selection_interval() to create a selection interval and add it to the scatter plot using add_params().")
        # Check if the histogram has been filtered by the selection
        transform_1 = chart_1.get('transform', [])
        has_filter_transform = False
        for transform in transform_1:
            if 'filter' in transform and 'param' in transform['filter']:
                has_filter_transform = True
                break
        if has_filter_transform:
            print_passed("The histogram has been filtered by the selection from the scatter plot.")
        else:
            print_failed("The histogram is not filtered by the selection from the scatter plot. You should use transform_filter() to filter the histogram based on the selected points in the scatter plot.")
    except:
        print_failed("Your solution did not generate the expected chart. Please follow the instructions and make sure you have created a scatter plot with the correct encoding channels, a histogram with the correct encoding channels, and linked them with a selection interval.")
        raise
