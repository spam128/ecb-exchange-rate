# ecb-exchange-rate
RSS scrapper reads course exchanges from European Central Bank


### Installation
Add exchange_scrapper folder as an app and include urls. 

In app directory exchange_scrapper there a Pipfile. Go there and type:
```pipenv install --python 3```
Make migrations
```python manage.py migrate'''

### Usage:
EP:
#Creates newest exchange log for example POST create/ name=JPY
*    POST create/ name=shortcut_exchange_name 
get all exchange logs for given exchange name for example GET USD/
*    GET shortcut_exchange_name/ 


#### remark: csrf is turned off
