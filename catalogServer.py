#!/usr/bin/env python3

from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import (
    Base,
    MenuItem,
    Restaurant
)

# Create session and connect to DB
# view sqlalchemy's 'create_engine' doc before changing parameter
engine = create_engine('postgresql:///catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


# landing page
@app.route("/")
def main():
    return render_template('index.html')


# create new menu item, cannot change item ID (primary key)
@app.route(
    "/restaurants.html/<int:restaurant_id>/new",
    methods=['GET', 'POST']
)
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'], course=request.form['course'],
            restaurant_id=restaurant_id
        )

        session.add(newItem)
        session.commit()
        flash("Menu item '{name}' has been deleted".format(name=newItem.name))
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

    return render_template('newMenuItem.html', restaurant_id=restaurant_id)


# del menu item, restaurant_id as param to redirect back to its menu page
@app.route("/restaurants.html/<int:restaurant_id>/<int:menu_id>/delete")
def delMenuItem(restaurant_id, menu_id):
    name = session.query(MenuItem).filter_by(id=menu_id).one().name
    session.query(MenuItem).filter_by(id=menu_id).delete()
    session.commit()
    flash("Menu item '{name}' has been deleted".format(name=name))
    return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))


# edit menu item, allowed to edit restaurant_id
# so as to move one item to another menu instead of del and recreating
@app.route(
    "/restaurants.html/<int:restaurant_id>/<int:menu_id>/edit",
    methods=['GET', 'POST']
)
def editMenuItem(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(
            id=menu_id).one()
    if request.method == 'POST':

        if request.form['name']:
            menuItem.name = request.form['name']

        if request.form['description']:
            menuItem.description = request.form['description']

        if request.form['price']:
            menuItem.price = request.form['price']

        if request.form['course']:
            menuItem.course = request.form['course']

        if request.form['restaurant_id']:
            menuItem.restaurant_id = request.form['restaurant_id']

        session.add(menuItem)
        session.commit()
        flash("Menu item '{name}' has been updated".format(name=menuItem.name))
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

    return render_template(
            'editMenuItem.html',
            restaurant_id=restaurant_id,
            menu_id=menu_id,
            menuItem=menuItem
           )


# populate restaurants template with db query results
@app.route("/restaurants.html/<int:restaurant_id>/")
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template(
        'restaurantMenu.html',
        restaurant=restaurant, items=items
    )


@app.route("/restaurants.html/")
def restaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


@app.route(
    "/restaurants.html/new",
    methods=['GET', 'POST']
)
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        flash(
            "Restaurant '{name}' has been created".format(
                name=request.form['name']
            )
        )
        return redirect(url_for('restaurants'))

    return render_template('newRestaurant.html')


@app.route("/restaurants.html/<name>/delete")
def delRestaurant(name):
    session.query(Restaurant).filter_by(name=name).delete()
    session.commit()
    flash("Restaurant '{name}' has been deleted".format(name=name))
    return redirect(url_for('restaurants'))


@app.route(
    "/restaurants.html/<name>/edit",
    methods=['GET', 'POST']
)
def editRestaurantName(name):
    if request.method == 'POST':
        edit = session.query(Restaurant).filter_by(name=name).one()
        edit.name = request.form['name']
        session.add(edit)
        session.commit()
        flash(
            "Restaurant '{name}' has been renamed to '{newName}'".format(
                name=name, newName=request.form['name']
            )
        )
        return redirect(url_for('restaurants'))

    return render_template('editRestaurantName.html', name=name)


if __name__ == '__main__':
    app.secret_key = 'dev_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=12345)
