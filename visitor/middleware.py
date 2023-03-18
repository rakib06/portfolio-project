from .models import Visitor

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.visitor_count = 0
        
    def __call__(self, request):
        
        visitor_ip = request.META.get('REMOTE_ADDR')
        visitor = Visitor(ip_address=visitor_ip)
        visitor.save()
        response = self.get_response(request)
        return response

    # def process_template_response(self, request, response):
    #     response.context_data["visitor_count"] = self.visitor_count
    #     return response
