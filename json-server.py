import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status

from views import get_all_orders, get_single_order, create_order, delete_order
from views import get_all_metals, get_single_metal, create_metal, delete_metal, update_metal
from views import get_all_sizes, get_single_size, create_size, delete_size, update_size
from views import get_all_styles, get_single_style, create_style, delete_style, update_style

class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for kneel diamonds"""

    def do_GET(self):
        """Handle GET requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            if url["pk"] != 0:
                response_body = get_single_order(url["pk"])
                if response_body:
                    return self.response(response_body, status.HTTP_200_SUCCESS.value)
                else:
                    return self.response("Requested resource not found.", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
            
            response_body = get_all_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "metals":
            if url["pk"] != 0:
                response_body = get_single_metal(url["pk"])
                if response_body:
                    return self.response(response_body, status.HTTP_200_SUCCESS.value)
                else:
                    return self.response("Requested resource not found.", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
            
            response_body = get_all_metals()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        elif url["requested_resource"] == "sizes":
            if url["pk"] != 0:
                response_body = get_single_size(url["pk"])
                if response_body:
                    return self.response(response_body, status.HTTP_200_SUCCESS.value)
                else:
                    return self.response("Requested resource not found.", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
            
            response_body = get_all_sizes()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        elif url["requested_resource"] == "styles":
            if url["pk"] != 0:
                response_body = get_single_style(url["pk"])
                if response_body:
                    return self.response(response_body, status.HTTP_200_SUCCESS.value)
                else:
                    return self.response("Requested resource not found.", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
            
            response_body = get_all_styles()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
        else:
            return self.response("Requested resource not found.", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
        
    def do_POST(self):
        url = self.parse_url(self.path)

        # Get the request body JSON for the new data
        content_len = int(self.headers.get('content-length', 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "orders":
            successfully_created = create_order(request_body)
            if successfully_created:
                return self.response(request_body, status.HTTP_201_SUCCESS_CREATED.value)

        elif url["requested_resource"] == "metals":
            successfully_created = create_metal(request_body)
            if successfully_created:
                return self.response(request_body, status.HTTP_201_SUCCESS_CREATED.value)
        
        elif url["requested_resource"] == "sizes":
            successfully_created = create_size(request_body)
            if successfully_created:
                return self.response(request_body, status.HTTP_201_SUCCESS_CREATED.value)

        elif url["requested_resource"] == "styles":
            successfully_created = create_style(request_body)
            if successfully_created:
                return self.response(request_body, status.HTTP_201_SUCCESS_CREATED.value)
        
        else:
            return self.response("Bad request data", status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value)
        
    def do_DELETE(self):
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            successfully_deleted = delete_order(url["pk"])
            if successfully_deleted:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
            
            return self.response("Requested resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
            
        elif url["requested_resource"] == "metals":
            successfully_deleted = delete_metal(url["pk"])
            if successfully_deleted:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
            
            return self.response("Requested resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

        elif url["requested_resource"] == "sizes":
            successfully_deleted = delete_size(url["pk"])
            if successfully_deleted:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)

        elif url["requested_resource"] == "styles":
            successfully_deleted = delete_style(url["pk"])
            if successfully_deleted:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)

            return self.response("Requested resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

        else:
            return self.response("Requested rsource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
    
    def do_PUT(self):
        url = self.parse_url(self.path)

        content_len = int(self.headers.get('content-length', 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "metals":
            successfully_updated = update_metal(url["pk"], request_body)
            if successfully_updated:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
            
        elif url["requested_resource"] == "sizes":
            successfully_updated = update_size(url["pk"], request_body)
            if successfully_updated:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)

        elif url["requested_resource"] == "styles":
            successfully_updated = update_style(url["pk"], request_body)
            if successfully_updated:
                return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
            
        else:
            return self.response("Requested resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
        
#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()