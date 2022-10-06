# Api doc 

-- auth/api/token/ 
    
    POST
    
    param: username, password


-- api/get-urls-list/

    GET
    AuthUser, AdminUser


-- api/create/

    POST
    param: link
    AuthUser, AdminUser


-- api/url-detail/<<id:post_id>>/
    
    GET, PUT, PATCH, DELETE
    AuthUser, AdminUser


-- api/<<slug:short_link>>/

    GET
