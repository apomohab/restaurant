from flask import Flask, render_template, request, redirect,jsonify, url_for, flash, make_response
from sqlalchemy import create_engine,asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
from flask import session as login_session
import random
import string
app = Flask(__name__)
# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import httplib2
import json
from flask import make_response
import requests





#Get google client_id for this app from json file

CLIENT_ID = json.loads(

	open('client_secrets.json', 'r').read())['web']['client_id']



engine = create_engine('sqlite:///myrestaurantapp.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


# ADD JSON API ENDPOINT HERE

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])





@app.route('/login', methods=['GET','POST'])

def showLogin():

	if request.method == 'GET':
		state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
		login_session['state'] = state
		return render_template('login.html', STATE=state)
	if request.method == 'POST':
		try:
			#Check the state variable for extra security
			print("step 0")
			if login_session['state'] != request.args.get('state'):
				response = make_response(json.dumps('Invalid state parameter.'), 401)
				response.headers['Content-Type'] = 'application/json'
				print("step 1")
				return response
			#Retrieve the token sent by the client
			token = request.data.decode('utf-8')
			print("step 2")
			#Request an access tocken from the google api
			idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), CLIENT_ID)
			print("step 3")
			url = (
				'https://oauth2.googleapis.com/tokeninfo?id_token=%s'
				% token)
			h = httplib2.Http()
			
			result = json.loads(h.request(url, 'GET')[1].decode("utf-8"))

			print("step 4")
			print(result['aud'])
			# If there was an error in the access token info, abort.
			if result.get('error') is not None:
				response = make_response(json.dumps(result.get('error')), 500)
				response.headers['Content-Type'] = 'application/json'
				return response
			print("step 5")
			# Verify that the access token is used for the intended user.
			user_google_id = idinfo['sub']
			if result['sub'] != user_google_id:
				response = make_response(
						json.dumps("Token's user ID doesn't match given user ID."),
						401)
				response.headers['Content-Type'] = 'application/json'
				return response
			print(result['sub'])
			# Verify that the access token is valid for this app.
			if result['aud'] != CLIENT_ID:
				print("step 5.5")
				response = make_response(
						json.dumps("Token's client ID does not match app's."), 401)
				print ("Token's client ID does not match app's.")
				response.headers['Content-Type'] = 'application/json'
				return response
			print("step 6")
			#Check if the user is already logged in
			stored_access_token = login_session.get('access_token')
			stored_user_google_id = login_session.get('user_google_id')
			if stored_access_token is not None and user_google_id == stored_user_google_id:
				response = make_response(
					json.dumps('Current user is already connected.'), 200)
				response.headers['Content-Type'] = 'application/json'
				return response
			print("step 7")
			# Store the access token in the session for later use.
			login_session['access_token'] = idinfo
			login_session['user_google_id'] = user_google_id
			# Get user info
			login_session['username'] = idinfo['name']
			login_session['picture'] = idinfo['picture']
			login_session['email'] = idinfo['email']

			return 'Successful'
		except ValueError:

			# Invalid token

			pass

#Logout
@app.route('/logout')
def Logout():
	login_session.clear()
	return redirect('/restaurants')


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):

    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items      = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    return render_template('menu.html', restaurant=restaurant, items=items)





#show all restaurants on home page.
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).order_by(asc(Restaurant.name))
    return render_template('restaurants.html', restaurants=restaurants)



#create new item
@app.route('/restaurants/<int:restaurant_id>/new',methods=['GET','POST'])
def NewItem(restaurant_id):
	if 'username' not in login_session:
		return redirect('/login')
		if request.method =='POST':
			addItem = MenuItem(name=request.form['name'], price=request.form['price'], description=request.form['description'], course=request.form['course'], restaurant_id = restaurant_id)
		session.add(addItem)
		flash('New Item  Successfully Created')
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('newitem.html',restaurant_id = restaurant_id)











#edit menu items

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit',methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
	if 'username' not in login_session:
			return redirect('/login')
	editItem = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editItem.name = request.form['name']
		if request.form['price']:
			editItem.price = request.form['price']
		if request.form['description']:
			editItem.description = request.form['description']
		if request.form['course']:
			editItem.tipe = request.form['course']
			session.add(editItem)
			flash('New Item  Successfully Edited')
			session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		return render_template('editmenu.html',restaurant_id=restaurant_id ,menu_id=menu_id, i=editItem)



#delete items
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete',methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
	itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
			session.delete(itemToDelete)
			flash('New Item  Successfully Deleted .')
			session.commit()
			return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
	else:
    		return render_template('delete.html', item=itemToDelete)




if __name__ == '__main__':

    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=4000, threaded=False)
