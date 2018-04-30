
(cl:in-package :asdf)

(defsystem "tg_package-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "observation_msg" :depends-on ("_package_observation_msg"))
    (:file "_package_observation_msg" :depends-on ("_package"))
  ))