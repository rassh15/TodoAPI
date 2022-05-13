# TodoAPI
## This is an ToDo API.
### Implement this API using django and rest framework and uses jwt token authorization.
#### User can create and View todo items where Admin user can perform CRUD operations.

### It have following APIs.

#### POST method for auth controller
## `/api/login/` ----> To login return access token and user details
## `/api/logout/` -----> Blacklist refresh token
## `/api/register/` -------> Create User\n


### All below api is for TodoController
### GET
## `/create` -----> it will create todo item have following fields {'tid','title','desc'}
### POST
## `/getall` ------> Return todoitems

### GET
## `/{id}`  ---------> get particular todo item
### PUT
## `/{id}` ----------> update particular todo item
### Delete
## `/{id}` ---------------? delete given todo item
