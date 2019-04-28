from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, CourseSection, CourseReport, Video, File, OrderItem, Order, Image, Category, Subcategory
from django.urls import reverse
# Create your views here.
app_name = 'courses'
