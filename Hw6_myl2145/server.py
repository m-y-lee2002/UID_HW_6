from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# Global keyword is only needed when modifying a global variable within a function.
top_three_list = [1, 2, 3]
sauces = {
    1:{
        "id": 1,
        "name": "Truff Hot Sauce Black Truffle Infused",
        "net_wt_oz": 6,
        "img": "truff_hot_sauce.jpg",
        "brand": "Truff",
        "rating_out_of_10": 9.2,
        "price": 17,
        "scoville_heat_unit":2700 , 
        "similar_heat":[] 	
    },
    2:{
        "id": 2,
        "name": "XXXTRA Hot Sauce Chile Habanero",
        "net_wt_oz": 4,
        "img": "xxxchilehabi.jpg",
        "brand": "El Yucateco",
        "rating_out_of_10": 6.5,
        "price": 3.39,
        "scoville_heat_unit":11500,
        "similar_heat":[] 
    },
    3:{
        "id": 3,
        "name": "The Last Dab Apollo",
        "net_wt_oz": 5,
        "img": "the_last_dab_apollo.jpg",
        "brand": "Hot Ones",
        "rating_out_of_10": 4,
        "price": 3.39,
        "scoville_heat_unit":2700000,
        "similar_heat":[] 
    },
    4:{
        "id": 4,
        "name": "Truff Hotter Sauce Black Truffle Infused",
        "net_wt_oz": 6,
        "img": "truff_hotter_sauce.jpg",
        "brand": "Truff",
        "rating_out_of_10": 5,
        "price": 17,
        "scoville_heat_unit":6000 , 
        "similar_heat":[5] 
    },
    5:{
        "id": 5,
        "name": "Black Label Reserve Chile Habanero",
        "net_wt_oz": 4,
        "img": "black_label_Yucateco.jpg",
        "brand": "El Yucateco",
        "rating_out_of_10": 7,
        "price": 3.39,
        "scoville_heat_unit":5000,
        "similar_heat":[4] 
    }

}
brands = {
   "El Yucateco":[2,5],
   "Truff":[1,4],
   "Hot Ones":[3]
}
def search_sauces(search_input):
    result = []
    for sauce in sauces.values():
        if search_input.lower() in sauce["name"].lower():
            result.append(sauce)
    return result
@app.route('/')
def landingPage():
    return render_template('landing_page.html', top_three_list=top_three_list, sauces=sauces)
@app.route('/search_result/<search_input>', methods=['GET'])
def searchResult(search_input):
    search_result = search_sauces(search_input)
    return render_template('search_result.html', search_result=search_result, search_input=search_input)
@app.route('/sauce/<int:sauce_id>')
def sauceDetail(sauce_id):
    target_sauce = sauces.get(sauce_id)
    if target_sauce:
        return render_template('sauce_detail.html', sauce=target_sauce, sauces=sauces, brands=brands)
    else:
        return "Sauce not found", 404
if __name__== '__main__':
    app.run(debug=True, port=5001)