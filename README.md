# Finance
Public repo for finances project.

More information of the website [upaspro](https://upaspro.com)

## Contents 

1. [cashflow](#cashflow). Link to the project


## Cashflow
Use a json file containing the income, expenses, and savings of your account in the following format for each month. 

This will give you some insight on what financial aspect you can work on.

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

