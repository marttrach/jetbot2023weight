Know_width = 15
#jetbot_width是bbox辨識的大小
def FocalLength(measured_distance,real_width,width_in_rf_image):
    focal_length = (width_in_rf_image* measured_distance)/ real_width
    return focal_length
def Distance_finder (Focal_Length, real_jetbot_width, jetbot_width_in_frame):
    distance = (real_jetbot_width* Focal_Length)/jetbot_width_in_frame
    return distance
 Distance = Distance_finder(308,Know_width,jetbot_width) #308是MX219焦距
