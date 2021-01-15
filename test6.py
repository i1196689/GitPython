import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import tensorflow as tf
from sklearn.metrics import confusion_matrix

print(tf.__version__)

##双通道
#初始化化权重
def weight_variable(shape,regularizer):
    w = tf.Variable(tf.truncated_normal(shape,stddev=0.1),tf.float32)#截断正态分布)
    if regularizer!= None:
        #将加权w引起的loss添加到损失函数losses对应位置
        tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(regularizer)(w))
    return w

#偏置
def bias_variable(shape):
    b = tf.Variable(tf.constant(0.1,shape=shape),tf.float32)
    return b

# 卷积层
def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_33(x):
    return tf.nn.max_pool(x,ksize=[1,3,3,1],strides=[1,3,3,1],padding='SAME')

def max_pool_22(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

def max_pool_11(x):
    return tf.nn.max_pool(x,ksize=[1,1,1,1],strides=[1,1,1,1],padding='SAME')

#随机获取一个batch数据，用于训练
def get_batch(train_x,train_y,batch,batch_size):
    start = batch*batch_size
    end = (batch+1)*batch_size
    # indice=np.random.choice(data_size,batch_size,False)
    batch_x=train_x[start:end]
    batch_y=train_y[start:end]
    return batch_x,batch_y

# def get_batch(train_x,train_y,batch):
#     """"返回n_batch对应的batch_size组数据"""
#     start = batch*batch_size
#     end = (batch+1)*batch_size
#     batch_x=train_x[start:end]
#     batch_y=train_y[start:end]
#     return batch_x,batch_y

##通道1
def CNN_net(x,REGULARIZER,keep_prob,conv_width=3):
    """默认卷积核尺寸为5"""
    with tf.name_scope('CNN0'):
        with tf.name_scope('w-conv0'):
            W_conv0 = weight_variable([1,1,1,16],REGULARIZER) # [w_height,w_width, num_channel,n_filters]
        with tf.name_scope('b-conv0'):
            b_conv0 = bias_variable([16]) #一个卷基层共享偏置
        with tf.name_scope('conv0'):
            conv0_Wx_plus_b = conv2d(x,W_conv0)+b_conv0

        with tf.name_scope('BN0'):   
            axis = list(range(len(conv0_Wx_plus_b.shape) - 1))
            conv0_wb_mean, conv0_wb_var = tf.nn.moments(conv0_Wx_plus_b, axis)
            conv0_scale  = tf.Variable(tf.ones([16]))
            conv0_offset = tf.Variable(tf.zeros([16]))
            variance_epsilon = 0.00001   
            bn0 = tf.nn.batch_normalization(conv0_Wx_plus_b, conv0_wb_mean, conv0_wb_var, conv0_offset, conv0_scale, variance_epsilon)

        with tf.name_scope('relu0'):
            h_conv0 = tf.nn.relu(bn0) #卷积结果加上偏置再过激活层 [batch_size,1,260,16]
        with tf.name_scope('max_pool0'):
            h_pool0 = max_pool_11(h_conv0) #池化 [batch_size,1,260,16]

    #第一层卷积 x:[batch_size,1,260,16]
    with tf.name_scope('CNN1'):
        with tf.name_scope('w-conv1'):
            W_conv1 = weight_variable([1,conv_width,16,32],REGULARIZER) # [w_height,w_width, num_channel,n_filters]
        with tf.name_scope('b-conv1'):
            b_conv1 = bias_variable([32]) #一个卷基层共享偏置
        with tf.name_scope('conv1'):
            conv1_Wx_plus_b = conv2d(h_pool0,W_conv1)+b_conv1

        with tf.name_scope('BN1'):   
            axis = list(range(len(conv1_Wx_plus_b.shape) - 1))
            conv1_wb_mean, conv1_wb_var = tf.nn.moments(conv1_Wx_plus_b, axis)
            conv1_scale  = tf.Variable(tf.ones([32]))
            conv1_offset = tf.Variable(tf.zeros([32]))
            variance_epsilon = 0.00001   
            bn1 = tf.nn.batch_normalization(conv1_Wx_plus_b, conv1_wb_mean, conv1_wb_var, conv1_offset, conv1_scale, variance_epsilon)

        with tf.name_scope('relu1'):
            h_conv1 = tf.nn.relu(bn1) #卷积结果加上偏置再过激活层 [batch_size,1,260,32]
        with tf.name_scope('max_pool1'):
            h_pool1 = max_pool_33(h_conv1) #池化 [batch_size,1,87,32]

    #第er层卷积
    with tf.name_scope('CNN2'):
        with tf.name_scope('w-conv2'):
            W_conv2 = weight_variable([1,conv_width,32,64],REGULARIZER) 
        with tf.name_scope('b-conv2'):
            b_conv2 = bias_variable([64]) #一个卷基层共享偏置
        with tf.name_scope('conv2'):
            conv2_Wx_plus_b = conv2d(h_pool1,W_conv2)+b_conv2

        with tf.name_scope('BN2'):   
            axis = list(range(len(conv2_Wx_plus_b.shape) - 1))
            conv2_wb_mean, conv2_wb_var = tf.nn.moments(conv2_Wx_plus_b, axis)
            conv2_scale  = tf.Variable(tf.ones([64]))
            conv2_offset = tf.Variable(tf.zeros([64]))
            variance_epsilon = 0.00001   
            bn2 = tf.nn.batch_normalization(conv2_Wx_plus_b, conv2_wb_mean, conv2_wb_var, conv2_offset, conv2_scale, variance_epsilon)

        with tf.name_scope('relu2'):
            h_conv2 = tf.nn.relu(bn2) #卷积结果加上偏置再过激活层  [batch_size,1,87,64]
        with tf.name_scope('max_pool2'):
            h_pool2 = max_pool_33(h_conv2) #池化 [batch_size,1,29,64]
        
    #第三层卷积
    with tf.name_scope('CNN3'):
        with tf.name_scope('w-conv3'):
            W_conv3 = weight_variable([1,3,64,128],REGULARIZER) 
        with tf.name_scope('b-conv3'):
            b_conv3 = bias_variable([128]) #一个卷基层共享偏置
        with tf.name_scope('conv3'):
            conv3_Wx_plus_b = conv2d(h_pool2,W_conv3)+b_conv3 

        with tf.name_scope('BN3'):   
            axis = list(range(len(conv3_Wx_plus_b.shape) - 1))
            conv3_wb_mean, conv3_wb_var = tf.nn.moments(conv3_Wx_plus_b, axis)
            conv3_scale  = tf.Variable(tf.ones([128]))
            conv3_offset = tf.Variable(tf.zeros([128]))
            variance_epsilon = 0.001   
            bn3 = tf.nn.batch_normalization(conv3_Wx_plus_b, conv3_wb_mean, conv3_wb_var, conv3_offset, conv3_scale, variance_epsilon)

        with tf.name_scope('relu3'):
            h_conv3 = tf.nn.relu(bn3) #卷积结果加上偏置再过激活层  [batch_size,1,29,128]
        with tf.name_scope('max_pool3'):
            h_pool3 = max_pool_22(h_conv3) #池化 [batch_size,1,15,128]

        #第四层卷积
    with tf.name_scope('CNN4'):
        with tf.name_scope('w-conv4'):
            W_conv4 = weight_variable([1,3,128,256],REGULARIZER) 
        with tf.name_scope('b-conv4'):
            b_conv4 = bias_variable([256]) #一个卷基层共享偏置
        with tf.name_scope('conv4'):
            conv4_Wx_plus_b = conv2d(h_pool3,W_conv4)+b_conv4 

        with tf.name_scope('BN4'):   
            axis = list(range(len(conv4_Wx_plus_b.shape) - 1))
            conv4_wb_mean, conv4_wb_var = tf.nn.moments(conv4_Wx_plus_b, axis)
            conv4_scale  = tf.Variable(tf.ones([256]))
            conv4_offset = tf.Variable(tf.zeros([256]))
            variance_epsilon = 0.001   
            bn4 = tf.nn.batch_normalization(conv4_Wx_plus_b, conv4_wb_mean, conv4_wb_var, conv4_offset, conv4_scale, variance_epsilon)

        with tf.name_scope('relu4'):
            h_conv4 = tf.nn.relu(bn4) #卷积结果加上偏置再过激活层  [batch_size,1,15,256]
        with tf.name_scope('max_pool4'):
            h_pool4 = max_pool_22(h_conv4) #池化 [batch_size,1,8,256]

    return h_pool4

def ful_net(h_pool4,num1=100,num2=40,num3=5):
    """全连接层  
      h_pool4:CNN_net的结果
      num1，num2, num3:各层神经网络的个数
    """
    
    #第一个全连接层
    with tf.name_scope('full_connect1'):
        with tf.name_scope('f_w1'):
            W_fc1 = weight_variable([1*8*256,num1],REGULARIZER) #num1个神经元
        with tf.name_scope('f_b1'):
            b_fc1 = bias_variable([num1])
        with tf.name_scope('reshape'):
            h_pool4_flat = tf.reshape(h_pool4,[-1,1*8*256])  
        # with tf.name_scope('fc1_BN'):
        #     axis = list(range(len(h_pool3_flat.shape) - 1))
        #     fc1_wb_mean, fc1_wb_var = tf.nn.moments(h_pool3_flat, axis)
        #     fc1_scale  = tf.Variable(tf.ones([1*33*128]))
        #     fc1_offset = tf.Variable(tf.zeros([1*33*128]))
        #     variance_epsilon = 0.00001   
        #     fc1_bn = tf.nn.batch_normalization(h_pool3_flat, fc1_wb_mean, fc1_wb_var, fc1_offset, fc1_scale, variance_epsilon)           
        with tf.name_scope('fc1_out'):
            h_fc1= tf.nn.relu(tf.matmul(h_pool4_flat,W_fc1) + b_fc1)
        with tf.name_scope('fc1_dropout'):
            h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

    with tf.name_scope('full_connect2'):
        with tf.name_scope('f_w2'):
            W_fc2 = weight_variable([num1,num2],REGULARIZER) #256个神经元
        with tf.name_scope('f_b2'):
            b_fc2 = bias_variable([num2])
        # with tf.name_scope('fc2_BN'):
        #     axis = list(range(len(h_fc1_drop.shape) - 1))
        #     fc2_wb_mean, fc2_wb_var = tf.nn.moments(h_fc1_drop, axis)
        #     fc2_scale  = tf.Variable(tf.ones([50]))
        #     fc2_offset = tf.Variable(tf.zeros([50]))
        #     variance_epsilon = 0.00001   
        #     fc2_bn = tf.nn.batch_normalization(h_fc1_drop, fc2_wb_mean, fc2_wb_var, fc2_offset, fc2_scale, variance_epsilon)         
        with tf.name_scope('fc2_out'):
            h_fc2= tf.nn.relu(tf.matmul(h_fc1_drop ,W_fc2) + b_fc2)
        with tf.name_scope('fc2_dropout'):
            h_fc2_drop = tf.nn.dropout(h_fc2,keep_prob)

    #输出层
    with tf.name_scope('full_Connect3'):
        with tf.name_scope('f_w3'):
            W_fc3 = weight_variable([num2,num3],REGULARIZER) #输出神经元
        with tf.name_scope('f_b3'):           
            b_fc3 = bias_variable([num3])
        with tf.name_scope('fc3_output'):
            #输出
            y_prediction =tf.nn.relu(tf.matmul(h_fc2_drop,W_fc3) + b_fc3)

    return y_prediction


#载入数据
print("Loading data and labels...")
# data_name=['intra_train_data1','intra_train_label1','intra_vali_data1','intra_vali_label1'] 
data_name=['train_data1','train_label1','vali_data1','vali_label1']
load_datas = [sio.loadmat(namex) for namex in data_name]
# print(load_datas)
for i in range(4):
    if i == 0 :
        train_data = load_datas[i][data_name[i]]  
        train_data =train_data.T  #(?,260)
        print(train_data.shape)
    if i ==1 :
        train_label = load_datas[i][data_name[i]] #(?,5)
        print(train_label.shape)
    if i ==2 :
        vali_data = load_datas[i][data_name[i]]
        vali_data = vali_data.T
        print(vali_data.shape)
    if i ==3:
        vali_label = load_datas[i][data_name[i]]
        print(vali_label.shape)
   
print("======================================")

##数据可视化
# print("shape of train_data"+str(train_data.shape))

# row0 = train_data[:,0]
# a = range(len(row0))
# #可视化心拍
# plt.plot(a,row0)
# plt.xlabel('sampling points')
# plt.ylabel('Amplitude/mV')
# plt.title('beat')
# ymin = 0.8*min(row0) if min(row0)>0 else 1.1*min(row0)
# ymax = 1.1*max(row0) if max(row0)>0 else 0.8*max(row0)
# plt.axis([1,260,ymin,ymax])
# plt.show()
print("Divide training and testing set...")
Indices1=np.arange(train_data.shape[0]) 
np.random.shuffle(Indices1) #arange(Indices)随机打乱索引

Indices2=np.arange(vali_data.shape[0]) 
np.random.shuffle(Indices2) 


#训练集与测试集随机打乱
train_x= train_data[Indices1] 
train_y= train_label[Indices1] 
vali_x = vali_data[Indices2]
vali_y = vali_label[Indices2]

print("======================================")

print("1D-CNN_net5 setup and initialize...")
input_node = 260
output_node  = 5
batch_size = 256 #批次大小
data_size = len(train_data )

n_batch = data_size//batch_size  # //整除， 训练多少个batch_size完成整个数据集的一次训练

LEARNING_RATE_BASE = 0.002
LEARNING_RATE_DECAY = 0.97
REGULARIZER = 0.0001 #正则化系数
MOVING_AVERAGE_DECAY = 0.99 #滑动平均

with tf.name_scope('inputs'):
    with tf.name_scope('x_input'):
        x=tf.placeholder(tf.float32, [None, 260]) #定义placeholder数据入口
    with tf.name_scope('y_output'):
        y=tf.placeholder(tf.float32,[None,5])


keep_prob = tf.placeholder(tf.float32)
x_reshaped=tf.reshape(x,[-1,1,260,1]) #[batch,n_height,n_width,n_channel]
h_pool1 = CNN_net(x_reshaped,REGULARIZER,keep_prob,conv_width=7)
h_pool2 = CNN_net(x_reshaped,REGULARIZER,keep_prob,conv_width=5)

#h_pool = tf.concat([h_pool1,h_pool2],axis=0,name='concat')
h_pool = h_pool1

y_prediction = ful_net(h_pool,100,40,5)

print(y_prediction.shape)

with tf.name_scope('training'):
    with tf.name_scope('loss'):
    #交叉熵
        ce  =  tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=y_prediction))
        cem = ce + tf.add_n(tf.get_collection('losses'))  #正则化loss
        tf.summary.scalar('loss',cem)

global_step = tf.Variable(0,trainable=False)  # 已运行batch_size 的轮数

with tf.name_scope('learning_rate'):
    learning_rate = tf.train.exponential_decay(   #指数衰减学习率
        LEARNING_RATE_BASE,
        global_step,  # 已运行batch_size 的轮数
        n_batch,   #多少轮batch_size更新一次学习率，即设计完成一次训练更新一次
        LEARNING_RATE_DECAY,
        staircase = True         
        )
    tf.summary.scalar('learning_rate',learning_rate)

with tf.name_scope('train_step'):
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(cem,global_step=global_step)

with tf.name_scope('ema'):
    #滑动平均
    ema = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
    ema_op = ema.apply(tf.trainable_variables())
    with tf.name_scope('train_op'):
        with tf.control_dependencies([train_step,ema_op]):
            train_op = tf.no_op(name='train')

with tf.name_scope('correct_prediction'):
    correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_prediction,1)) #布尔型 
with tf.name_scope('acc'):    
    acc = tf.reduce_mean( tf.cast(correct_prediction,'float') )  #正确率, reduce_mean:求平均值

#合并指标,loss & acc
merged = tf.summary.merge_all()

print("1D-CNN_net5 training processing...")
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
   
    writer = tf.summary.FileWriter('logs/',sess.graph)  #tensorboard图生成路径 d当前目录下的logs文件夹
    for epoch in range(1,201): #整个数据集训练的次数
        
        for batch in range(n_batch):  # n_batch:对训练数据集完成一次训练，即一个epoch，一共有多少batch
            #获得一个批次的图片及标签
            batch_x,batch_y=get_batch(train_x,train_y,batch,batch_size) #一次取batch_sie组数据
            _, loss,step,train_accuracy,summary= sess.run([train_op,cem,global_step,acc,merged],feed_dict={x:batch_x,y:batch_y,keep_prob:0.6})

        # #完成一个 Epoch 训练过程后，对训练数据随机 Shuffle 打乱训练数据顺序
        # indexx = np.random.shuffle(np.arange(data_size) ) #arange(Indices)随机打乱索引
        # train_x= train_data[indexx] 
        # train_y= train_label[indexx] 
       
        writer.add_summary(summary,epoch) #，每完成一次训练，写入一次summary
        
        if  epoch % 5 == 0:
            #训练10个epoch后de准确率
            vali_accuracy,vali_loss = sess.run([acc,cem],feed_dict={x:vali_x, y:vali_y, keep_prob:1.0})
            print("After "+str(epoch)+" training，train accuracy is: "+str(train_accuracy)+", train loss is: "+ str(loss)+", validation accuracy is: "+str(vali_accuracy)+", validation loss is: "+ str(vali_loss))
          

    
    y_pred=y_prediction.eval(feed_dict={x:vali_x,y:vali_y,keep_prob:1.0})

    y_pred=np.argmax(y_pred,axis=1)
    y_true=np.argmax(vali_y,axis=1)

    Acc=np.mean(y_pred==y_true)
    Conf_Mat=confusion_matrix(y_true,y_pred) #利用专用函数得到混淆矩阵
    Acc_N=Conf_Mat[0][0]/np.sum(Conf_Mat[0])
    Acc_S=Conf_Mat[1][1]/np.sum(Conf_Mat[1])
    Acc_V=Conf_Mat[2][2]/np.sum(Conf_Mat[2])
    Acc_F=Conf_Mat[3][3]/np.sum(Conf_Mat[3])
    Acc_U=Conf_Mat[4][4]/np.sum(Conf_Mat[4])

    print('\nTesting----------------------')
    print('Test Accuracy=%.3f%%'%(Acc*100))
    print('Accuracy_N=%.3f%%'%(Acc_N*100))
    print('Accuracy_S=%.3f%%'%(Acc_S*100))
    print('Accuracy_V=%.3f%%'%(Acc_V*100))
    print('Accuracy_F=%.3f%%'%(Acc_F*100))
    print('Accuracy_U=%.3f%%'%(Acc_U*100))
    print('\ntesting Confusion Matrix:')
    print(Conf_Mat)
    print("=================================================================")


    # for i in range(411*10): # batch_size训练次数：training_steps 
    #         start = (i * batch_size) % data_size
    #         end = min(start + batch_size, data_size)

    #         # 每次选取batch_size个样本进行训练

    #         # _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: trainx[start: end], y_: trainy[start: end]})
    #         # _, step = sess.run([train_op, global_step], feed_dict={x: train_x[start: end], y_: train_y[start: end]})
    #         _, loss,step,train_accuracy = sess.run([train_op,cem,global_step,acc],feed_dict={x:train_x[start: end], y:train_y[start: end],keep_prob:0.6})
    #         if i % 411 == 0:
    #             print("train_accuracy: "+ str(train_accuracy))

# tf.expand_dims(input_tensor, 1)

