# Backend of the feedback application

## Documentation for calls

---
<br/>

### **Login with Microsoft**
<br/>

<ins> General information </ins>

>* Route: `/login_microsoft`
>* Methods: `POST`

<ins> Parameters </ins>:

>* accessToken `{string}` `[body]`

<ins> Returns </ins>:

>* jwtToken `{string}`
>* email `{string}`
>* name `{string}`

```
{
    "jwtToken": "andlnawlaw32525kwnlkn.awdawjdo115m.fdnalnfd",
    "email": "example_email@outlook.com",
    "name": "Firstname Lastname"
}
```

<ins> Purpose </ins>:

* A user is logged in to Microsoft by use of the received `accessToken`. If the user
does not already exist in the database, the user is created based on the email and 
name received from Microsoft when logging in. An email is always present, as this is
used to login with, however the name of the user received from Microsoft can be empty.
If this is the case, `None/nill` is returned in the `name`, instead of an empty string.

---
<br/>

### **Get Microsoft events from Outlook calendar**
<br/>

<ins> General information </ins>

>* Route: `/get_microsoft_events`
>* Methods: `POST`

<ins> Parameters: </ins>

>* x-access-token `{string}` `[header]`
>* accessToken `{string}` `[body]`

<ins> Returns: </ins>

* `response` object which for each meeting contains:
>* id `{string}`
>* subject `{string}`
>* bodyPreview `{string}`
>* startTime `{string in ISO 8601 UTC format}`
>* endTime `{string in ISO 8601 UTC format}`
>* location `{string}`
>* attendees `{list of object(s)}`
>   * email `{string}`
>   * name `{string}`

```
{
    "response": [
        {
            "attendees": [
                {
                    "email": "email1@outloook.com",
                    "name": "Firstname1 Lastname1"
                },
                {
                    "email": "email2@outlook.com",
                    "name": "Firstname2 Lastname2"
                }
            ],
            "bodyPreview": "A description of the scheduled meeting",
            "endTime": "2022-01-04T11:30:00Z",
            "id": "AQMkADAwYjQxLTA1L7qaFAoaDaFAJIaTsABQbAAA=",
            "location": "SomePlace",
            "startTime": "2022-01-04T11:00:00Z",
            "subject": "The subject of the meeting"            
        },
        {
            "attendees": [
                {
                    "email": "email1@outloook.com",
                    "name": "Firstname1 Lastname1"
                },
                {
                    "email": "email2@outlook.com",
                    "name": "Firstname2 Lastname2"
                },
                {
                    "email": "email3@outlook.com",
                    "name": "Firstname3 Lastname3"
                },
                {
                    "email": "email4@outlook.com",
                    "name": "Firstname4 Lastname4"
                }
            ],
            "bodyPreview": "A description of the scheduled meeting",
            "endTime": "2022-10-20T11:30:00Z",
            "id": "AQMkADAwYjQxLTA1L7qaFAoaDaFAJIaTsABQbAAA=",
            "location": "SomePlace",
            "startTime": "2022-10-20T11:45:00Z",
            "subject": "The subject of the meeting"            
        }
    ]
}
```


<ins> Purpose: </ins>

* The events of a users Outlook calendar is fetched from Microsoft. If the `accessToken`
used to log in to Microsoft has expired, an error corresponding to the received Microsoft
error will be returned. 

---
<br/>

### **Create event**
<br/>

<ins> General information </ins>

>* Route: `/create_event`
>* Methods: `POST`

<ins> Parameters: </ins>

>* x-access-token `{string}` `[header]`
>* title `{string}` `[body]` `(required)`
>* startDate `{string}` `[body]` `(required)`
>* endDate `{string}` `[body]` `(required)`
>* description `{string}` `[body]` 
>* questions `{list of strings}` `[body]`

<ins> Returns: </ins>

* Nothing (empty object)
```
{}
```


<ins> Purpose: </ins>

* A logged in user can create an event with the parameters described above. A unique pin
will be added to the event, while it remains active. This pin can be used by other
non-logged-in users, to give feedback on the questions asked by the creator of the event.
See [submit_feedback](Placeholder) ##FUNCTIONALITY YET TO BE IMPLEMENTED.

---
<br/>

### **Modify or delete an event**
<br/>

<ins> General information </ins>

>* Route: `/modify_event`
>* Methods: `PUT, DELETE`

<br/>

If Method is <ins>__PUT__ </ins>:

<ins> Parameters </ins>:

>* x-access-token `{string}` `[header]` `(required)`
>* ID `{string}` `[body]` `(required)`
>* title `{string}` `[body]`
>* startDate `{string}` `[body]`
>* endDate `{string}` `[body]`
>* description `{string}` `[body]`

<ins> Returns </ins>:

>* Nothing (empty object)
```
{}
```

<br/>

If Method is <ins>__DELETE__ </ins>:

<ins> Parameters </ins>:

>* x-access-token `{string}` `[header]` `(required)`
>* ID `{list of strings}` `[body]` `(required)`

<ins> Returns </ins>:

>* Nothing (empty object)
```
{}
```

<ins> Purpose </ins>:

__PUT__:
* Given the `ID` of an existing event, this allows the owner of the event to change the 
contents of said event.
Parameters available to be changed/overwritten, as listed above, are:
    * `title`
    * `startDate`
    * `endDate`
    * `description`

__DELETE__:
* Given the `ID(s)` of an existing event, this allows the owner of an event to delete the
event(s) corresponding to the `ID(s)`, along with every question and given feedback 
associated with the event(s).


---
<br/>

### **Modify or delete a question**
<br/>

<ins> General information </ins>

>* Route: `/modify_question`
>* Methods: `PUT, DELETE`

<br/>

If Method is <ins>__PUT__ </ins>:

<ins> Parameters </ins>:

>* x-access-token `{string}` `[header]` `(required)`
>* ID `{string}` `[body]` `(required)`
>* description `{string}` `[body]`

<ins> Returns </ins>:

>* Nothing (empty object)
```
{}
```

<br/>

If Method is <ins>__DELETE__ </ins>:

<ins> Parameters </ins>:

>* x-access-token `{string}` `[header]` `(required)`
>* ID `{list of strings}` `[body]` `(required)`

<ins> Returns </ins>:

>* Nothing (empty object)
```
{}
```

<ins> Purpose </ins>:

__PUT__:
* Given the `ID` of an existing question belonging to an event, this allows the owner of 
the event to change the description of the question.
Parameter available to be changed/overwritten, as listed above, are:
    * `description`

__DELETE__:
* Given the `ID(s)` of existing question(s), this allows the owner of an event to delete 
the question(s) corresponding to the `ID(s)`, along with all given feedback 
associated with the question(s).
