# Download market data! Educational Finance's API Project.

The following project was made for educational purposes to extract stock values on the stock market from the Invertir Online website.

The educational project aims to teach how to extract data from the web, using the requests library, and how to parse the data using the BeautifulSoup library. The project also aims to show how to create a package in Python, and how to publish the package in the Python Package Index (PyPI).

The project use differents libraries, CI/CD tools, and other tools to make the project more professional. The project uses libraries like requests, BeautifulSoup, pandas, and others.

# Developer Mode

## Standard setup

Get the code

```bash
git clone git@github.com:LeanoA/iolpy.git && cd iolpy
```

Setup de developer enviroment
```bash
mamba env create -f development.yml
conda activate iolpy-dev
```
    
Install the package in developer mode
```bash
cd .. # Go to the root of the project
pip install -e iolpy
```

where `iolpy` is the name of the package, and `iolpy-dev` is the name of the environment. At the same time `iolpy` is the name of the folder where the package is located. It is installed in developer mode(flag `-e`), so any changes made to the code will be reflected in the package. For more information about the installation process, see the [https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/).

## Code test
To code test, you can use the following command:
```bash
pytest
```
or
```bash
python -m pytest
```
The difference between the two commands is that the first command uses the pytest library, and the second command uses the Python interpreter to run the pytest module. The two commands are equivalent. 

Alternativaly, it is posible to use tox to run the tests. To run the tests with tox, use the following command:
```bash
tox
```
The tox command will run the tests in different environments.

Other commands can be use to test if the package can be imported with minimal dependencies:
```bash
tox -e import-minimal
```
