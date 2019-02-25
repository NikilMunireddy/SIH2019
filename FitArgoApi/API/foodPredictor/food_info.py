import json

FOOD_INFO_FILE_PATH='./foodItem.json'

def food_calorie(item):
    with open(FOOD_INFO_FILE_PATH) as f:
        data = dict(json.load(f))
    try:
        res=data[item]
    except IndexError as e:
        res=e
    return res

if __name__ == "__main__":
    food_name='dal'
    print(json.dumps(food_calorie(food_name),indent=2))