;; Auto-generated. Do not edit!


(when (boundp 'tg_package::observation_msg)
  (if (not (find-package "TG_PACKAGE"))
    (make-package "TG_PACKAGE"))
  (shadow 'observation_msg (find-package "TG_PACKAGE")))
(unless (find-package "TG_PACKAGE::OBSERVATION_MSG")
  (make-package "TG_PACKAGE::OBSERVATION_MSG"))

(in-package "ROS")
;;//! \htmlinclude observation_msg.msg.html


(defclass tg_package::observation_msg
  :super ros::object
  :slots (_observation ))

(defmethod tg_package::observation_msg
  (:init
   (&key
    ((:observation __observation) "")
    )
   (send-super :init)
   (setq _observation (string __observation))
   self)
  (:observation
   (&optional __observation)
   (if __observation (setq _observation __observation)) _observation)
  (:serialization-length
   ()
   (+
    ;; string _observation
    4 (length _observation)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _observation
       (write-long (length _observation) s) (princ _observation s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _observation
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _observation (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get tg_package::observation_msg :md5sum-) "23dfd6d60034bead10f6625ddcde1df9")
(setf (get tg_package::observation_msg :datatype-) "tg_package/observation_msg")
(setf (get tg_package::observation_msg :definition-)
      "string observation

")



(provide :tg_package/observation_msg "23dfd6d60034bead10f6625ddcde1df9")


