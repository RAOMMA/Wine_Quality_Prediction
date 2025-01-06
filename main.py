import argparse
import joblib

# Load the pre-trained logistic regression model
model = joblib.load('C:/salman/ML/Red Wine Quality/model.pkl')

# Create an argument parser
parser = argparse.ArgumentParser(description="wine quality perdection")

# Add the --value argument to accept a data record
parser.add_argument('--fixed_acidity', type=float, required=True, help='fixed_acidity')
parser.add_argument('--volatile_acidity', type=float, required=True, help='volatile_acidity')
parser.add_argument('--citric_acid', type=float, required=True, help='citric_acid')
parser.add_argument('--residual_sugar', type=float, required=True, help='residual_sugar')
parser.add_argument('--chlorides', type=float, required=True, help=	'chlorides')
parser.add_argument('--free_sulfur_dioxide', type=float, required=True, help='free_sulfur_dioxide')
parser.add_argument('--total_sulfur_dioxide', type=float, required=True, help='total_sulfur_dioxide')
parser.add_argument('--density', type=float, required=True, help='density')
parser.add_argument('--pH', type=float ,required=True, help='pH')
parser.add_argument('--sulphates', type=float, required=True, help='sulphates')
parser.add_argument('--alcohol', type=float, required=True, help='alcohol')

# Parse the command-line arguments
args = parser.parse_args()


# Parse the data record as a list of floats
data_list =[[args.fixed_acidity,args.volatile_acidity,args.citric_acid,args.residual_sugar,args.chlorides,args.free_sulfur_dioxide,args.total_sulfur_dioxide,args.density,args.pH,args.sulphates,args.alcohol]]

#predict
pred=model.predict(data_list)[0]

print(f'Winr quality is {pred}')