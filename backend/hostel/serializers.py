from rest_framework import serializers
from .models import *
from authentication.serializers import UserSerializer

class HostelSerializer(serializers.ModelSerializer):
    available_rooms = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Hostel
        fields =  ['id', 'name', 'location', 'room_type', 'is_veg', 'is_non_veg', 'gender', 
                  'person_per_room', 'no_of_rooms', 'total_capacity', 
                  'room_description', 'image', 'available_rooms', 'amount', 'bathroom_type']
    
    def get_amount(self, obj):
        year = self.context.get('year')
        std_type = self.context.get('quota')
        return obj.get_amount(year, std_type)
        # # 3 : Govt
        # # 3 : Mgmt
        # print(f"{year} : {std_type}")
        # amounts = {
        #     1: {
        #         "govt": obj.first_year_fee_mgmt
        #     }
        # }
        # return 0
        # if year == 1:
        #     return obj.first_year_fee
        # elif year == 2:
        #     return obj.second_year_fee
        # elif year == 3:
        #     return obj.third_year_fee
        # elif year == 4:
        #     return obj.fourth_year_fee
        
        # return obj.first_year_fee

    def get_available_rooms(self, obj):
        return obj.available_rooms()
    
class RoomBookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    hostel = HostelSerializer(read_only=True)

    class Meta:
        model = RoomBooking
        fields = ['id', 'user', 'hostel', 'status', 'payment_expiry', "booked_at", "payment_completed_at", "food_type"]