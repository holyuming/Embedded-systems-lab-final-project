import pyautogui
import argparse
import sys
import jetson.inference
import jetson.utils


import time
import statistics

parser = argparse.ArgumentParser(description="Run pose estimation DNN on a video/image stream.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.poseNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="/dev/video0", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="resnet18-hand", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="links,keypoints", help="pose overlay flags (e.g. --overlay=links,keypoints)\nvalid combinations are:  'links', 'keypoints', 'boxes', 'none'")
parser.add_argument("--threshold", type=float, default=0.15, help="minimum detection threshold to use") 





try:
    opt = parser.parse_known_args()[0]
    print(opt.network, opt.input_URI)
   
except:
    # print("")
    # parser.print_help()
    sys.exit(0)

# load the pose estimation model
net = jetson.inference.poseNet(opt.network, sys.argv, opt.threshold)



# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv)


pyautogui.FAILSAFE = False

x_list,y_list=[0],[0]
stdx = stdy = 100

# process frames until the user exits
while True:
    time1 = time.time()
    
    # capture the next image
    img = input.Capture()

    # perform pose estimation (with overlay)
    poses = net.Process(img, overlay=opt.overlay)

    # print the pose results
    # print("detected {:d} objects in image".format(len(poses)))

    x = 0   
    y = 0

    for pose in poses:
        # idx = 12
        # mid = pose.Keypointw[idx]
        # print(mid)
        #break
        x=0
        y=0
        count = 0
        if(len(x_list)>10):
            x_list.pop(0)

        if(len(y_list)>10):
            y_list.pop(0)
        

        xmin = 0
        ymin = 0

        for key in pose.Keypoints:
            if ymin < key.y:
                xmin = key.x
                #if ymin > key.y:
                ymin = key.y
            x += key.x
            y += key.y
            count += 1
            # if count == 8:
            #    x += key.x
            #    y += key.y


        x -= xmin
        y -= ymin
        count -= 1

        x = x/count
        y = y/count

        x_list.append(x)
        y_list.append(y)

        if (len(x_list) > 10):
            stdx, stdy = statistics.pstdev(x_list), statistics.pstdev(y_list)
            print(stdx, stdy)

        break

    if (stdx < 3 and stdy < 3):
        pyautogui.click(button="left")
        x_list.clear()
        y_list.clear()
        stdx = 100
        stdy = 100

    pyautogui.moveTo(1920-x*1.5, y*1.45)    #     print(pose)
    #     wrist_idx = 0
    #     middle_finger_idx = 12
    #     if wrist_idx < 0 or middle_finger_idx < 0:
    #         continue
    #     wrist = pose.Keypoints[wrist_idx]
    #     middle_finger = pose.Keypoints[middle_finger_idx]
    #     point_x = (wrist.x + middle_finger.y)/2
    #     point_y = (wrist.y + middle_finger.y)/2

    #     print(point_x,point_y)
    #     pyautogui.moveTo(point_x, point_y)

        # print(type(pose))
        # print(pose.Keypoints)
        # print('Links', pose.Links)

    # print(net.GetNetworkFPS())
    # render the image
    output.Render(img)

    # update the title bar
    output.SetStatus("{:s} | Network {:.0f} FPS X:{:f} Y:{:f}".format(opt.network, net.GetNetworkFPS(), x, y))

    # print out performance info
    net.PrintProfilerTimes()

    # exit on input/output EOS
    if not input.IsStreaming() or not output.IsStreaming():
        break

