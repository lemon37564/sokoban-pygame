class UnknowIdentifierError(Exception):
    pass

__maps = [
# map 0 (exception, debugging)
"""
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPP    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPP    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPP.$@ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPP   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
""",

# map 1
"""
HHHHHHHHHHHHHHHHHHHHHHHHHH
H########################H
H#.########  !     $.####H
H# ########$  ###### ####H
H# ########  $######!####H
H# ######  $ $ ##### ####H
H#$###### # ## ##### ####H
H# ####   # ## #####  ..#H
H# ####    $      $   ..#H
H# ########!### #@##  ..#H
H#!             #### ####H
H########################H
HHHHHHHHHHHHHHHHHHHHHHHHHH
""",

# map 2
"""
HHHHHHHHHHHHHHHHHHHHH 
H          !#!      H 
H $   ##########    H 
H# ## #       ####  H 
H# ##   $#$#@  #    H 
H  ##  !   $ #   $ #H 
H   #%#  ######## ##H 
H   ##! .....   # ##H 
H## ##  .....   # ##H 
H  $#########  ##$  H 
H   #  !#   #   #   H 
H   $   #  !#   $   H 
H!  #       $   #   H 
H   #   #   #   #  !H 
HHHHHHHHHHHHHHHHHHHHH 
""",

# map 3
"""
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
H##################################H
H#####           !     .......... #H
H##!       #     ##    #  $  #### #H
H#####    ###  ####  ######   ### #H
H###  $   #                 #     #H
H###!#     $ #####$   ###       ###H
H# $ # ##### ###      #   ##### ###H
H#      ##        #####       ! ###H
H###   ###@##$##    !  $  ####  ###H
H#####  ###   #     ####   $    ###H
H#! ## $  #           ##  ! ###$###H
H#            ##    !  #          #H
H##################################H
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
""",

# map 4
"""
HHHHHHHHHHHHHHHHHHHHHHHHH
H #####  #  ####.$     .H
H !#    $   # ! #  !   $H
H  #  ## ## $$# ####### H
H ### ##  # #    !  ### H
H    $  $  $#$ #### ### H
H !   #  ## #    ... ## H
H ## ### # @    #... ## H
H    $  $  ###  #... ## H
H  !  #    #          ! H
H  ## #  #    ###     ##H
H!     !   #   !   #  ! H
HHHHHHHHHHHHHHHHHHHHHHHHH
""",

# map 5
"""
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
H@     ##   #      #    # # # #     H
H# $# #  !     ##    ##         ### H
H#    #    ###     #     # ####     H
H# ##    ##      #  #  # #  !    # #H
H    #      # ##    #    # #   #   #H
H   #  ### ##  ## #   # #    #  #   H
H##        ###       #    #   #    #H
H     #  #  #  # # #    ##  #    # #H
H ##  ##  #     # # #   ### ##   # #H
H ###    #  #    !    ## #     ###  H
H      #      #     #      #   #.   H
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
""",

# map 6
"""
HHHHHHHHHHHHHHHHHHHHHHHHH
H! ##  #! ##  !        !H
H      #  #      ###### H
H    ! #  # $#  $     ! H
H .#.# # ## @#   # #### H
H . .    #  $# ##     ! H
H .#.# # # $    #  #### H
H . . $  ##  ##       ! H
H .#.# #  #   ## $ ## # H
H    $  $        # $ $ .H
H   #    ######      .# H
H!  ######    #      ## H
H $    #    #  $    ### H
H    !      ##         !H
HHHHHHHHHHHHHHHHHHHHHHHHH
""",

# map 7
"""
HHHHHHHHHHHHHHHHHHHHHHH
H.... #@###    # !   %H
H....        #$$  #   H
H.... ##   ### #  #  !H
H....   #  ### ## ##  H
H.   ## #     $ $ #   H
H  !    # !##$ $  #!  H
H ##$## ####  # ##### H
H!      ##    # #    !H
H$     ### #  $    ###H
H  ##   #    $ $ #    H
H%!#%   # ## ## $   ! H
H###%    $$     $$    H
H%%##    $ ### ## ### H
H!         #!     #!  H
HHHHHHHHHHHHHHHHHHHHHHH
""",

# map 8
"""
HHHHHHHHHHHHHHHHHHHHHHH
H!            !     !#H
H  ###   #    #   ...#H
H  # $ # # ##$   .....H
H  #  $  #  $    .....H
H ## # # #  #!   .....H
H #  # # $  $ #       H
H  !## ## $## #     #!H
H #   $  $ #    $   ##H
H #$ ####  # ### ##   H
H !   $   $      $ $  H
H ######## $##$    $  H
H  $    .##      ##   H
H##########  !   #   @H
HHHHHHHHHHHHHHHHHHHHHHH
""",

# map 9
"""
HHHHHHHHHHHHHHHHHHHHHHHH
H###...########  ######H
H###.       $ # $    .#H
H###$ $######!#.......#H
H#$#$  #.#### # $ $$$ #H
H$  $$$   ### # $  $  #H
H $$$  $$.### # ##### #H
H#  $  $ #### #      $#H
H#   #####   !####### #H
H#$ $!   !       $   @#H
H    ##           ### #H
H# $ .####!   ! #####$#H
H# #$$  .##########   #H
H#. $    ##!    $     #H
H#### $.###  $$$    ...H
H####   .## $    P  ...H
HHHHHHHHHHHHHHHHHHHHHHHH
"""
]

__count = len(__maps)

# 取得第index關
def get_map(index: int) -> str:
    if index < 0 or index >= __count:
        print("map index out of range")
        return __maps[0]
    return __maps[index]

# 關卡總數
def level_count() -> int:
    return __count