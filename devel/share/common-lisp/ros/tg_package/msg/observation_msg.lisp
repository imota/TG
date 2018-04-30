; Auto-generated. Do not edit!


(cl:in-package tg_package-msg)


;//! \htmlinclude observation_msg.msg.html

(cl:defclass <observation_msg> (roslisp-msg-protocol:ros-message)
  ((observation
    :reader observation
    :initarg :observation
    :type cl:string
    :initform ""))
)

(cl:defclass observation_msg (<observation_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <observation_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'observation_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tg_package-msg:<observation_msg> is deprecated: use tg_package-msg:observation_msg instead.")))

(cl:ensure-generic-function 'observation-val :lambda-list '(m))
(cl:defmethod observation-val ((m <observation_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tg_package-msg:observation-val is deprecated.  Use tg_package-msg:observation instead.")
  (observation m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <observation_msg>) ostream)
  "Serializes a message object of type '<observation_msg>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'observation))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'observation))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <observation_msg>) istream)
  "Deserializes a message object of type '<observation_msg>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'observation) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'observation) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<observation_msg>)))
  "Returns string type for a message object of type '<observation_msg>"
  "tg_package/observation_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'observation_msg)))
  "Returns string type for a message object of type 'observation_msg"
  "tg_package/observation_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<observation_msg>)))
  "Returns md5sum for a message object of type '<observation_msg>"
  "23dfd6d60034bead10f6625ddcde1df9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'observation_msg)))
  "Returns md5sum for a message object of type 'observation_msg"
  "23dfd6d60034bead10f6625ddcde1df9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<observation_msg>)))
  "Returns full string definition for message of type '<observation_msg>"
  (cl:format cl:nil "string observation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'observation_msg)))
  "Returns full string definition for message of type 'observation_msg"
  (cl:format cl:nil "string observation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <observation_msg>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'observation))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <observation_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'observation_msg
    (cl:cons ':observation (observation msg))
))
