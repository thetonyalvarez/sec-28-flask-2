### Conceptual Exercise

Answer the following questions below:

-   What is RESTful routing?

    -   It's a way to standardize the architecture of web services

-   What is a resource?

    -   An object with a type, associated data, relationships to other resources

-   When building a JSON API why do you not include routes to render a form that when submitted creates a new user?

    -   Because JSON can only represent dictionaries, lists, and primitive types. It cannot represent things like SQLAlchemy models.

-   What does idempotent mean? Which HTTP verbs are idempotent?

    -   It's an operation that can be executed many times with the same data, and you get the same return every time.
    -   `GET`, `PUT/PATCH`, `DELETE` are all idempotent operations

-   What is the difference between PUT and PATCH?

    -   `PUT` updates the entire resource
    -   `PATCH` updates the a _part_ of the resource

-   What is one way encryption?

    -   Encryption that can only be hashed one-way, and cannot be reversed and decoded

-   What is the purpose of a `salt` when hashing a password?

    -   A random string that's concatenated to the password before hashing to further encrypt the password

-   What is the purpose of the Bcrypt module?

    -   It hashes and salts a password in our app using the bcrypt algorithm.

-   What is the difference between authorization and authentication?
    -   Authentication verifies the identity of a user.
    -   Authorization determines if said user can access some or all of our app.
