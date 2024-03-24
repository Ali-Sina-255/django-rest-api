from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Article
from .Api.serializers import ArticleSerializer


from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class ArticleListCreateApiView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailApiView(APIView):
    def get_object(self, value_from_url):
        article = get_object_or_404(Article, id=value_from_url)
        # this is our articel we will update or delete or just retrieve
        return article

    def get(self, request, value_from_url):
        article = self.get_object(value_from_url)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, value_from_url):
        article = self.get_object(value_from_url)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, value_from_url):
        article = self.get_object(value_from_url)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function base views
@api_view(["GET", "POST"])
def article_list_api_view(reqeust):
    if reqeust.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif reqeust.method == "POST":
        serializer = ArticleSerializer(data=reqeust.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "PUT", "DELETE"])
def article_detail_api_view(reqeust, value_from_url):
    try:
        article = Article.objects.get(id=value_from_url)
    except Article.DoesNotExist:
        return Response(
            {"error": {
                "code": 404,
                "message": f"there is no such table with the {value_from_url}."
            }},
            status=status.HTTP_404_NOT_FOUND
        )
    if reqeust.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    if reqeust.method == "PUT":
        serializer = ArticleSerializer(instance=article, data=reqeust.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if reqeust.method == "DELETE":
        article.delete()
        return Response({
            "process": {
                "code": 204,
                "message": f"Article whose id was {value_from_url} has been deleted"
            }}, status=status.HTTP_204_NO_CONTENT
        )


# class base views
