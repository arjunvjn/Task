from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile
from .serializer import UserProfileSerializer
from rest_framework.views import APIView
from django.core.paginator import Paginator

# Create your views here.

@api_view(['GET','POST'])
def users(request):
    if request.method=='GET':
        # user_list=UserProfile.objects.all()
        # return Response((UserProfileSerializer(user_list,many=True)).data)
        user_list=UserProfile.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(user_list, 5)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return Response((UserProfileSerializer(users,many=True)).data)
    else:
        serializer=UserProfileSerializer(data=request.data)
        if int(request.data['zip'])>0 and int(request.data['age'])>0:
            if serializer.is_valid():
                serializer.save()
                user=UserProfile.objects.all().order_by('-id')[0]
                return Response((UserProfileSerializer(user,many=False)).data)
            else:
                return Response({'error':serializer.error})
        else:
                return Response({'error':'Age or Zip is Negative'})

@api_view(['GET'])
def get_user_details(request,id):
    try:
        user=UserProfile.objects.get(pk=int(id))
        return Response((UserProfileSerializer(user,many=False)).data)
    except:
        return Response({'error':'User Not Found'})

@api_view(['PUT'])
def edit_user_profile(request,id):
    try:
        user=UserProfile.objects.get(pk=int(id))
        serializer=UserProfileSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response((UserProfileSerializer(user,many=False)).data)
        else:
            return Response({'error':serializer.error})
    except:
        return Response({'error':'User Not Found'})

@api_view(['DELETE'])
def delete_user(request,id):
    try:
        user=UserProfile.objects.get(pk=int(id))
        user.delete()
        return Response({'Success':'User Deleted'})
    except:
        return Response({'error':'User Not Found'})

@api_view(['GET'])
def search_users(request,name):
    user_list=UserProfile.objects.filter(first_name__icontains=name)
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return Response((UserProfileSerializer(users,many=True)).data)

@api_view(['GET'])
def sort_users(request,name):
    try:
        user_list=UserProfile.objects.all().order_by(name)
        page = request.GET.get('page', 1)
        paginator = Paginator(user_list, 5)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return Response((UserProfileSerializer(users,many=True)).data)
    except:
        return Response({'error':'Field not Found'})
