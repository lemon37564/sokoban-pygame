import logging

__maps = [
    # map 0 (exception, debugging)
    """
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP#!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPP    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPP    ##!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPP.$@ ##!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPP   ##!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP#!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HPPPPPP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!H
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
""",

# map 1 TUTORIAL
    """
HHHHHHHHHHHHHHHHHHHHHHHHHH
H       H              $.H               
H@   H        HHHHHHHHH HH                                     
HHHHHHHHHHHHHHP         HH
H           PHHHHHHHHHHHHH
H  HHHHHHHHHHHHHHHHHHHHHHH
H           H            H
H           H H          H
H$          H H          H
H.            H         PH
HHHHHHHHHHHHHHHHHHHHHHHHHH
HPH    H       H         H
H         H            !PH
HHHHHHHHHHHHHHHHHHHHHHHHHH
HP            #      .#H
H    ##  $   ##   ### #H
HHHHH                  H
HHHHHHHHHHHHHHHHHHHH  HHHH
HHHHHHHHHHHHHHHHHHHHHHHHHH
 """,

    # map 2
    """
HHHHHHHHHHHHHHHHHHHHHHHHHH
H########################H
H#. @ .$ ##        $.   #H
H#       ##$   ##### ## #H
H#  $   ###  $######!## #H
H#     ##  $  ######    #H
H# ###### # ######## ##$#H
H# #! ##  # ########  ..#H
H# #  ##   $      $   ..#H
H# #  #####!### # ##  ..#H
H#             !#### ####H
H########################H
HHHHHHHHHHHHHHHHHHHHHHHHHH
""",

    # map 3
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

    # map 4
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

    # map 5
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

    # map 6
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

    # map 7
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

    # map 8
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

    # map 9
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

    # map 10
    """
HHHHHHHHHHHHHHHHHHHHHHHH
H###...########  ######H
H###.       $ # $    .#H
H###$ $######!#.......#H
H#$#$  #.##P  # $ $$$ #H
H$  $$$   # # # $  $  #H
H $$$  $$.# # # #####$#H
H#  $  $ ## # #      @#H
H#P  #####   !#  ######H
H#$ $!   !    # $     #H
H    ##      ##   ### #H
H# $ .####!  ##. ####$#H
H# #$$  .### ######   #H
H#. $    ##     $     #H
H#### $.###  $$$    ...H
H####   .## $       ...H
HHHHHHHHHHHHHHHHHHHHHHHH
"""

]

# 扣掉第0關
__count = len(__maps) - 1

TUTORIAL = 1

# 取得第index關，超出範圍或<0則回傳第零關
def get_map(index: int) -> str:
    if index < 0 or index > __count:
        logging.warning(f"map index out of range({index}), set to default map (map 0)")
        return __maps[0]
    return __maps[index]

# 關卡總數
def level_count() -> int:
    return __count
