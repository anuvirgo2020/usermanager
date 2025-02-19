from flask import request, jsonify
from flask_restful import Resources 
from models import user 
from db import db

class UserRoutes(Resources):
    def __init__():
        pass
    def get(self, userid=None):
        if userid:
            user = User.query.get(userid)
            if user:
                return jsonify({
                    "userid":user.userid,
                    "first_name":user.first_name,
                    "last_name":user.last_name,
                    "username":user.username,
                })
            return jsonify({"message": "User not found"}), 404
        users = User.query.all()
        return jsonify([
            {
                    "userid":user.userid,
                    "first_name":user.first_name,
                    "last_name":user.last_name,
                    "username":user.username,
            } for user in users ])
        
    def post(self):
        data = request.get_json()
        new_user = User(
            first_name = data['first_name'],
            last_name = data['last_name'],
            username = data['username'],
            password = data['password'],
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"})

    def put(self, userid):
        user = User.query.get(userid)
        if not user:
            return jsonify({"message": "User not found"}), 404
        data = request.get_json()
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.username = data.get("username", user.username)
        user.password = data.get("password", user.password)      
        db.session.commit()
        return jsonify ({"message": "User updated successfully"})

    def delete(self, userid):
        user = User.query.get(userid)
        if not user:
            return jsonify ({"message": "User not found"})
        db.session.delete(user)
        db.session.commit()
        return jsonify ({"message": "User deleted successfully"})
