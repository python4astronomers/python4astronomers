#create new figure
figure(1)
clf()

#this contains the mixing ratio plot
subplot(210)
nruns=500
axis([0,nruns, 0, 1])

#this contains the box with the balls
subplot(211)
axis([-10, 10, -10, 10])

#vertical size of the gap between left and right side of the box
GapWidth=2.0

#plot internal wall
plot(array([0,0]),array([-10,-GapWidth/2]),linewidth=6,color='green')
plot(array([0,0]),array([GapWidth/2,10]),linewidth=6,color='green')

# Define properties of the "bouncing balls"
n = 100

#1 for red balls, 2 for blue
pos1 = (10 * random_sample(n*2) - 10).reshape(n, 2)
pos1[:,1]=pos1[:,1]*2+10.0
vel1 = (0.3 * normal(size=n*2)).reshape(n, 2)
pos2 = (10 * random_sample(n*2)).reshape(n, 2)
vel2 = (0.3 * normal(size=n*2)).reshape(n, 2)
pos2[:,1]=pos2[:,1]*2-10.0

#ball size is uniform
sizes=150*ones(n)

# Colors where each row is (Red, Green, Blue, Alpha).  Each can go
# from 0 to 1.  Alpha is the transparency.

colors1=zeros([n,4])
colors1[:,0]=1 #red
colors1[:,3]=1

colors2=zeros([n,4])
colors2[:,2]=1 #blue
colors2[:,3]=1

# Draw all the circles and return an object ``circles`` that allows
# manipulation of the plotted circles.
subplot(211)
circles1 = scatter(pos1[:,0], pos1[:,1], marker='o', s=sizes, c=colors1)
circles2 = scatter(pos2[:,0], pos2[:,1], marker='o', s=sizes, c=colors2)


#array to store the time evolution of the mixing ratio
mixratio=zeros(nruns,dtype='float')
#"time" i.e. number of runs 
xarray=range(nruns)

#title of mix plot
Title="Mixing ratio (#red/#blue on right hand side)"

for i in range(nruns):

    #stores old positions
    opos1=pos1
    opos2=pos2

    #omputes new positions
    pos1 = pos1 + vel1
    pos2 = pos2 + vel2


    # these are collisions of bals agains the inner wall - but not if in the gap
    collision1x= ( ((opos1[:,0] < 0) & (pos1[:,0] > 0)) | ((opos1[:,0] > 0) & (pos1[:,0] < 0))) & (abs(pos1[:,1]) > GapWidth/2)
    collision2x= ( ((opos2[:,0] < 0) & (pos2[:,0] > 0)) | ((opos2[:,0] > 0) & (pos2[:,0] < 0))) & (abs(pos2[:,1]) > GapWidth/2)


    # check if a bounce happens at boundaries or inner wall
    bounce1x = (abs(pos1[:,0]) > 10.0) | collision1x
    bounce1y = (abs(pos1[:,1]) > 10.0) 
    bounce2x = (abs(pos2[:,0]) > 10.0) | collision2x
    bounce2y = (abs(pos2[:,1]) > 10.0) 


    #bounces balls as needed in either x or y direction
    vel1[bounce1x,0] = -vel1[bounce1x,0]
    vel1[bounce1y,1] = -vel1[bounce1y,1]

    #bounced ball not only reverse veloctiy, but also are placed at the location
    #they were pre-bounce
    pos1[bounce1x]=opos1[bounce1x]

    circles1.set_offsets(pos1)    # Change the positions

    #bounces balls as needed in either x or y direction
    vel2[bounce2x,0] = -vel2[bounce2x,0]  
    vel2[bounce2y,1] = -vel2[bounce2y,1]
    
    #bounced ball not only reverse veloctiy, but also are placed at the location
    #they were pre-bounce
    pos2[bounce2x]=opos2[bounce2x]

    circles2.set_offsets(pos2)    # Change the positions

    #select upper plot
    subplot(211)

    #plot balls
    draw()

    #compute mixing ratio = #red/#blue in right hand side
    mixratio[i]=(pos1[(pos1[:,0] > 0)]).size/float((pos2[(pos2[:,0] > 0)]).size)
    
    #select lower plots and set it up and plot mixing ratio
    aaa=subplot(210)
    aaa.clear()
    aaa.axis([0,nruns, 0, 1])
    aaa.set_title(Title)
    aaa.plot(xarray,mixratio)


#that's all folks!
