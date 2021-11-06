import logging

__maps = [
    
# map 0 TUTORIAL
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
HP            #      .#HHH
H    ##  $   ##   ### #HHH
HHHHH                  HHH
HHHHHHHHHHHHHHHHHHHH  HHHH
HHHHHHHHHHHHHHHHHHHHHHHHHH
 """,

    # map 1
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

TUTORIAL = 0

# 取得第index關，超出範圍或<0則回傳第零關
def get_map(index: int) -> str:
    if index >1000:
        return 
    if index < 0 or index > __count:
        logging.warning(f"map index out of range({index}), set to default map (map 0)")
        return __maps[0]
    return __maps[index]

# 關卡總數
def level_count() -> int:
    return __count
