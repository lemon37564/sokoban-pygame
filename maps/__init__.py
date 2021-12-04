import logging
import maps.sokobanSolver
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
HP            # !    .#HHH
H    ##  $   ##   ### #HHH
HHHHH                  HHH
HHHHHHHHHHHHHHHHHHHH !HHHH
HHHHHHHHHHHHHHHHHHHHHHHHHH
 """,
  # map 1 Portal required 
 """
HH#####H
###   #H
#.  $ #H
###@$ #H
#.##$ #H
#$#P. ##
# $. $.#
#P$ . .#
##  ####
HHHHHHHH
"""
    ,
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
,
#map 11, random 8x8 map 
"""
HHHHHHHHH
H  #   #H
H @ $ ##H
H$    ##H
H.# ##.#H
H     $#H
H. #   #H
HHHHHHHHH
"""
,#map 12 random 8x8 map
"""
HHHHHHHHH
H#     #H
H  $@  #H
H . $  #H
H  # ###H
H   .###H
H. $  ##H
HHHHHHHHH
"""
,#map 13 random 8x8 map 
"""
HHHHHHHHH
H@ # # #H
H..$   #H
H  $   #H
H  #  ##H
H$  ####H
H  .   #H
HHHHHHHHH
"""
,#map 14 random 8x8 map
"""
HHHHHHHH
H ##   H
H      H
HH.  H.H
H @ $$ H
H   $  H
H #. # H
HHHHHHHH
"""
]

# 扣掉第0關
__count = len(__maps) - 1

TUTORIAL = 0

RANDOM_6X6 = 10000
RANDOM7X7 = 10001
RANDOM8X8 = 10002

def level_is_random(level: int) -> bool:
    """return True if this level is random generated"""
    return level >= RANDOM_6X6

def convertRandomLevel(input, size):
    level = input
    s = ""
    rowcount = 0
    for row in level:
        if(rowcount == 0 or rowcount == size - 1):
            s += "H" * (size+1) + '\n'
        else:
            s+= ("H" + row[1:size] + "H\n")
            print(rowcount)
        rowcount += 1
    s=s.replace('&','@')
    
    s=s.replace('B','$')
    s='\n'+s
    print(s)
    return s

# 取得第index關，超出範圍或<0則回傳第零關
def get_map(index: int) -> str:
    if index == RANDOM_6X6:
        return convertRandomLevel(maps.sokobanSolver.generate(6), 6)
    elif index == RANDOM7X7:
        return convertRandomLevel(maps.sokobanSolver.generate(7), 7)
    elif index == RANDOM8X8:
        return convertRandomLevel(maps.sokobanSolver.generate(8), 8)
        
    if index < 0 or index > __count:
        logging.warning(f"map index out of range({index}), set to default map (map 0)")
        return __maps[0]
    return __maps[index]

# 關卡總數
def level_count() -> int:
    return __count

if __name__ == '__main__':
    maps.sokobanSolver.generate()
    convertRandomLevel()
    get_map(1)
