# Finance
Public repo for finances project.

More information of the website [upaspro](https://upaspro.com)

## Contents 

1. [Setup](#Setup) 
2. [cashflow](#cashflow). Link to the project


## Setup

You first need to set the environment:

```Shell
git clone git@github.com:pagand/finance.git
pip install virtualenv 
python3 -m venv venv
```

Depending on your kernel apply one to activate the environment:

```Shell
source venv/bin/activate #for Mac/linux
.\venv\Scripts\activate.bat # for windows
```

Then you need to install the requirement packages:

```Shell
pip install -r requirements.txt # everytime
```


## Cashflow
Use a json file containing the income, expenses, and savings of your account in the following format for each month. 

This will give you some insight on what financial aspect you can work on.

You need to create this file and name it file.json and put it in the Cashflow directory.

```json
{
"January":{
  "Income": {
    "source 1" : {
        "date1": <value>,
        "date2": <value>,
         ...},

    "source 2" : {
        "date1": <value>,
        "date2": <value>,
         ...},
     ...
  }
   
  "Savings": {
    "transfer in" : {
        "date1": <value>,
        "date2": <value>,
         ...},
     "transfer out" : {
        "date1": <value>,
        "date2": <value>,
         ...},
      ...
  }

  "Expenses": {
    "category 1" : {
        "date1": <value>,
        "date2": <value>,
         ...},
     "Investments" : {
        "date1": <value>,
        "date2": <value>,
         ...},
      ...
  }
},

"February": {
...

}, 

...


}
```

