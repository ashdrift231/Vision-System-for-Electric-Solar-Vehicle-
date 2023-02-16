"""
This code uses the OpenCV library to capture video from the default camera and perform image processing to detect the line. 
It first converts the frame to grayscale and threshold it to get a binary image. 
It then finds the contours in the binary image and selects the largest one as the line. 
The code calculates the centroid of the contour and uses its position to determine the direction to move (left or right). 
The processed frame is displayed in a window and the loop continues until the 'q' key is pressed.
This is just a basic example and you may need to modify the code to suit your specific requirements, 
such as adjusting the threshold value, adding additional image processing steps, 
or changing the way the direction is determined.
"""

import cv2
import numpy as np

# Open the video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video feed
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image to get a binary image
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Find the contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        
        # Calculate the centroid of the contour
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            # Draw the contour and centroid on the frame
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            
            # Determine the direction to move based on the location of the centroid
            if cx < frame.shape[1] / 2:
                direction = "left"
            else:
                direction = "right"
                
            # Print the direction to move
            print("Move:", direction)
            
    # Show the processed frame
    cv2.imshow("frame", frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()


"""Sure, here's an example of how you can perform image processing to detect the line in a live video feed and determine the direction to move:

python

import cv2
import numpy as np

# Open the video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the video feed
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold the grayscale image to get a binary image
    _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Find the contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        
        # Calculate the centroid of the contour
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            # Draw the contour and centroid on the frame
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            
            # Determine the direction to move based on the location of the centroid
            if cx < frame.shape[1] / 2:
                direction = "left"
            else:
                direction = "right"
                
            # Print the direction to move
            print("Move:", direction)
            
    # Show the processed frame
    cv2.imshow("frame", frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()

