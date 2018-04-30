# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "tg_package: 1 messages, 0 services")

set(MSG_I_FLAGS "-Itg_package:/home/icaro/workspace/TG/src/tg_package/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(tg_package_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg" NAME_WE)
add_custom_target(_tg_package_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "tg_package" "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(tg_package
  "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tg_package
)

### Generating Services

### Generating Module File
_generate_module_cpp(tg_package
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tg_package
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(tg_package_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(tg_package_generate_messages tg_package_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg" NAME_WE)
add_dependencies(tg_package_generate_messages_cpp _tg_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tg_package_gencpp)
add_dependencies(tg_package_gencpp tg_package_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tg_package_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(tg_package
  "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tg_package
)

### Generating Services

### Generating Module File
_generate_module_eus(tg_package
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tg_package
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(tg_package_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(tg_package_generate_messages tg_package_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg" NAME_WE)
add_dependencies(tg_package_generate_messages_eus _tg_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tg_package_geneus)
add_dependencies(tg_package_geneus tg_package_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tg_package_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(tg_package
  "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tg_package
)

### Generating Services

### Generating Module File
_generate_module_lisp(tg_package
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tg_package
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(tg_package_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(tg_package_generate_messages tg_package_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg" NAME_WE)
add_dependencies(tg_package_generate_messages_lisp _tg_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tg_package_genlisp)
add_dependencies(tg_package_genlisp tg_package_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tg_package_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(tg_package
  "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/tg_package
)

### Generating Services

### Generating Module File
_generate_module_nodejs(tg_package
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/tg_package
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(tg_package_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(tg_package_generate_messages tg_package_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg" NAME_WE)
add_dependencies(tg_package_generate_messages_nodejs _tg_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tg_package_gennodejs)
add_dependencies(tg_package_gennodejs tg_package_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tg_package_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(tg_package
  "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tg_package
)

### Generating Services

### Generating Module File
_generate_module_py(tg_package
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tg_package
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(tg_package_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(tg_package_generate_messages tg_package_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/icaro/workspace/TG/src/tg_package/msg/observation_msg.msg" NAME_WE)
add_dependencies(tg_package_generate_messages_py _tg_package_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(tg_package_genpy)
add_dependencies(tg_package_genpy tg_package_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS tg_package_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tg_package)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/tg_package
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(tg_package_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tg_package)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/tg_package
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(tg_package_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tg_package)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/tg_package
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(tg_package_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/tg_package)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/tg_package
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(tg_package_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tg_package)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tg_package\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tg_package
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tg_package
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/tg_package/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(tg_package_generate_messages_py std_msgs_generate_messages_py)
endif()
