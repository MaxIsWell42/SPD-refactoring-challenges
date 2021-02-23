# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholesterol = 70
ldl = 30
triglyceride = 120

def cholesterol_level(total_cholesterol):
    if total_cholesterol < 200:
        return "low"
    elif 200 < total_cholesterol < 240:
        return "medium"
    else:
        return "high"

def ldl_level(ldl):
    if ldl < 130:
        return "low"
    elif 130 < ldl < 160:
        return 'medium'
    else: 
        return 'high'
    
def triglyceride_level(triglyceride):
    if triglyceride < 150:
        return 'low'
    elif 150 <= triglyceride < 200:
        return 'medium'
    else:
        return 'high' 

if cholesterol_level(total_cholesterol) == 'low' and ldl_level(ldl) == 'low' and triglyceride_level(triglyceride) == 'low':
    # good level
    print('*** Good level of cholestrol ***')
elif cholesterol_level(total_cholesterol) == 'medium' or ldl_level(ldl) == 'medium' or triglyceride_level(triglyceride) == 'medium':
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
elif cholesterol_level(total_cholesterol) == "high" or ldl_level(ldl) == "high" or triglyceride_level(triglyceride) == "high":
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
else:
    print('Error: unhandled case.')
