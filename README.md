Hi all,

I have produced an extension to ead’s and nedned’s code (thank you both very much!).

The package versions I used are:

- Python 3.6.5
- Django 2.0.2
- dash 0.21.1
- dash-core-components 0.22.1 
- dash-html-components 0.10.1                  
- dash-renderer 0.12.1
- numpy 1.14.3

The key differences are outlined below:

- This is a Django app with Django controlling the page navigation, context and data models with a Dash incorporated in to a page
- The database can be queried from a Dash layout using Django models and context. In the EU, this type of functionality is useful in staying compliant with GDPR regulations
- Separation of Dash and Django files to try and make it more discoverable (since they aren’t cleanly interleaved)
- There is also a filthy function called: “clean_dash_content”, which essentially gets rid of characters such as ‘\n’ in the content returned by Flask.
- Since most servers I have seen are offline, the Dash is served locally, which you can see in dash_server.py. This upset the CSS path that Dash tries to find so you will also notice that I put the Dash css in the ‘static’ folder and served it to fix this problem.
- Since the base pathname might not be known in advance, I changed the “display_page” function which loops through each layout function name to check whether it is in the url  - the applicable function is then returned. There may be an easier way using regex but I didn’t have the regex chops to do this at the time.

- Lines 14 to 21 in dash_layouts.py show how context is extracted from the url and used in a Django model.
- Lastly, if you look at the dash_django_page.html, you will see how the Dash content is injected:
{{ dash_content | safe}}. The “safe” keyword is critical in rendering the content.


The downside to this whole approach is the double handling of Flask and Django. However, I have hooked this Django app to MS IIS to serve pages and haven’t noticed a problem yet. I imagine the Flask dev instance might would fall over under heavy load.

I think a more professional, integrated approach between Dash and Django is highly desirable moving forward. However, I need to prove to my stakeholders at work that there is value in our system (which heavily relies on Django) before I can approach the firm to get fundnig for Plotly to help with this as a project.

I am eager to receive any feedback from the community and any ways to improve the code!
