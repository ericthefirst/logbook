#!/usr/bin/python 

import os;
import cgitb;
import cgi;
import sys;

cgitb.enable()

IMG_DIR = "img"

print("Content-type: text/html\r\n\r\n")
print("<html>")
print("\t<head>")
print("\t\t<title>Logbook</title>")
print("\t\t<meta charset='utf-8'>")

print("\t\t<style>")

print("\t\t\ttable,thead,th,td { ")
print("\t\t\t\tborder: none;")
#print("\t\t\t\tborder: 1px solid #888888;")
print("\t\t\t\tborder-collapse: collapse;")
print("\t\t\t}")

print("\t\t\tbody {")
print("\t\t\tbackground-color: #339999;")
print("\t\t\t}")
print("\t\t\ttable {")
print("\t\t\tbackground-color: #00aa88;")
print("\t\t\t}")

print("\t\t\ttr.title {")
print("\t\t\tbackground-color: #55bbdd;")
print("\t\t\t}")

print("\t\t\ttr.title > td {")
print("\t\t\t\tpadding: 0 10px 0;")
print("\t\t\t}")

print("\t\t\ttable {")
print("\t\t\t\tborder: none;")
print("\t\t\t}")

print("\t\t\ttd { ")
print("\t\t\t\tpadding: 15px 20px 0px 0px;")
print("\t\t\t\tfont-size: 40px;")
print("\t\t\t}")

print("\t\t\t.title {")
print("\t\t\t\tfont-family: Helvetica;")
print("\t\t\t\tfont-size: 60;")
print("\t\t\t}")

print("\t\t\ttr.title > td {")
print("\t\t\t\tfont-size: 60px;")
print("\t\t\t}")

print("\t\t\ttr.data > td {")
print("\t\t\t\tpadding-bottom: 80px")
print("\t\t\t}")

print("\t\t\t.comments {")
print("\t\t\t\tvertical-align: text-top;")
print("\t\t\t}")

print("\t\t\t#new, #new:visited, a, a:visited {")
print("\t\t\t\tpadding: 10px;")
print("\t\t\t\tposition: fixed;")
print("\t\t\t\tright: 10px;")
print("\t\t\t\tbottom: 10px;")
print("\t\t\t\tcolor: white;")
print("\t\t\t\tfont-family: Helvetica, Arial, sans-serif;")
print("\t\t\t\tfont-size: 14px;")
print("\t\t\t\ttext-decoration: none;")
print("\t\t\t\tbackground-color: rgba(28, 180, 240, .5 );")
print("\t\t\t\tborder: 3px solid rgba(20, 240, 220, .9);")
print("\t\t\t}")

print("\t\t</style>")
print("\t</head>")
print("\t<body>")
print("\t\t<table>")


with open("records", 'r') as f:
	lines = f.readlines()
lines.reverse()

for line in lines:
	if line[0] == "#":
		continue
	tokens  = line.split('\t')
	title    = tokens[0]
	comments = tokens[1]
	print('\t\t\t<tr class="title"><td colspan="2">{0}</td></tr><tr class="data"><td><img style="width:400px" src="{1}/{2}"></td><td class="comments">{3}</td></tr></div>'.format(title, IMG_DIR,title + ".png", comments))
print("\t\t</table>")
print("\t<a id='new' href='upload/upload_portal.html'>New entry</a>")
print("\t</body>")
print("</html>")

