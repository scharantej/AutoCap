## Automotive Website Design Using Flask

### HTML Files
- **index.html**: This HTML file will serve as the homepage of the website. It will contain the necessary elements for user interaction, such as a form for searching cars and a navigation bar.
- **car_details.html**: This HTML file will display detailed information about a specific car. It will include features such as the car's make, model, year, and price.

### Routes
- **@app.route('/')**: This route will handle the homepage of the website. It will load the index.html file and display it to the user.
- **@app.route('/car_details/<car_id>')**: This route will handle the display of detailed information about a specific car. It will take the car's ID as a parameter and use it to retrieve the necessary information from the database. The retrieved data will then be displayed in the car_details.html file.