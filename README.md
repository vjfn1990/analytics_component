# Analytics Component

Python/Django approach, that implements an Analytics Component with some Unit Tests

## Installation and execution

If 'virtualenv' is not installed on the system as a pip package, do the following:

```bash
pip install virtualenv
```

Check the correctness of the installation using:

```bash
virtualenv --version
```

Clone the repo using the following command:

```bash
git clone https://github.com/vjfn1990/analytics_component.git
```

Move to the root directory of the project:

```bash
cd analytics_component
```

Create a Virtual Environment using the following command:

```bash
virtualenv projectenv
```

Activate the Virtual Environment executing:

```bash
. projectenv/bin/activate
```

Notice that there is a 'dot' and a 'space' at the beginning of the command above. Now the Virtual Environment should be active, showing '(projectenv)' at the beginning of the command prompt.

Install the dependencies needed by the project (these dependencies aren't installed on the system but on the brand new Virtual Environment). Execute:

```bash
pip install -r requirements.txt
```

Move to the directory called 'myproject':

```bash
cd myproject
```

This is where there is a file called 'manage.py'. Make all the migrations needed by the Django ORM Model, executing the following commands:

```bash
python manage.py makemigrations myapp
python manage.py migrate
```

To deploy the webapp, do the following:

```bash
python manage.py runserver 0.0.0.0:8686
```

Any other available port for localhost, could be used.

## Preprocessing tasks

The execution of the following endpoints is slow, because all the information stored on the CSV files, needs to be mapped into the Django ORM Models. However, these are preprocessing tasks, so they need to be done only once.

The Pandas package is used to support these tasks.

On a web browser, type:

```bash
http://localhost:8686/myapp/fill_order_model
```

This endpoint will take the content of 'orders.csv' available at 'myapp/data/orders.csv' and store it over the Django ORM Models.

On a web browser, type:

```bash
http://localhost:8686/myapp/fill_order_line_model
```

This endpoint will take the content of 'order_lines.csv' available at 'myapp/data/order_lines.csv' and store it over the Django ORM Models.

## Retrieving tasks

Only the retrieval of the total number of items sold on a day was implemented, to be able to invest the time needed to build the other structural components of the webapp.

On a web browser, type:

```bash
http://localhost:8686/myapp/generate_report?date=2019-08-01
```

The specified date on the URL is given as an example, so any other one could be tested, even invalid ones.

For the example given, the endpoint would return '{"items": 121}', because 121 items were sold on August 1st, 2019.

## Unit Tests

On the 'myapp/' directory, there is a file called 'tests.py' where some Unit Tests were implemented. These can be executed using the following command:

```bash
python manage.py test
```

To be able to run the tests, the webapp has to be listening on another console tab, as it was shown before with the command:

```bash
python manage.py runserver 0.0.0.0:8686
```
