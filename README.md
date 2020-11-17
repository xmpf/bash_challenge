# Jail Bash

```
                              .     @$* @$3
                             '$Nueeed$$ed$$eeec$$
          ,            4$Lze@*$C2$b* ed(he*rb$CC$*$bc@$r              
    /@ |~~            .e$$"W$$B$B$**  ^$  e""##d?$Bd$$$Nc. ..      @\/~\ 
    \==|         4$kd*Cr$6F#"`  **   .*==      # '"**F#$I$b$*       |   I
       |         d$5N@$$"   ....eu$$$$$$N$*$zbeuu     #$d$$$$b.     / @/
      @/     . z$Ted*"$P zue$*9d$$$@##  .  #W$e@B$$L.    "#@$E$b@N
            #d$Id*P#  'Nd$$B$**"       .*,     "#*N$$b$c   $$$*$$c
           .d#+C6J   @@$B$*"          -***-        "#$$$$c   *$$$#$u
        ..u$l4@"^"zJ$7W*"              '*`            ^*$@$$$r "$$E$@B>
        *@$l$P"+Rd$$N#"          *     /|\     *        '"$$$c.. ?E$*b
        z$ "*.  .Jz$"           ***   / | \   ***         '*@N$b   d**N
      .z$JBR^bs@$$#          *   *   /  |  \   *  *         "$l*9N "bN$Nee
     4$$.C*   dB@"          ***    _/  /^\  \_   ***         '$$$z> 3$b$$#
      $"$e$  @*$"        *   *     \\^|   |^//    *   *        $$$u.^*$N$c
     JPd$%  @@d"        ***        ***********       ***       '$Ni$  $EP$
   :e$"*$  :et$          *         ***********        *         ^$$E  4$N$be
   ')$ud"  @6$                                                   9$$   $*@$"
    @F*$   *4P                    YOUR INPUT IS                  '$m#   .$$.
 u*""""""""""""h                   TRANSFORMED                  e#""""""""""#
 E +e       ue. N                                               4F e=c     z*c
 E +e       ue. N               $ tr [a-z] [A-Z]                4F e=c     z*c          ...
 #e$@e.. ..z6+6d"                ***************               ^*cBe$u.  .$$@
    $ ^"""" 4F"  ze=eu              ********              z***hc ^"$ ""*"" $            while (counter++ < MAX_TRIES) {
    $       ^F :*    3r               ****               @"  e "b  $       $                input = getpass("> ");
  .e$        N $  'be$L...             **             ...?be@F  $F $       9F               char *p = input;
 4" $        $ $.  zm$*****h.                      ue""""*h6   J$" $       4%               size_t len = 0;
 $  $        $ $$u5e" .     "k                    d"       #$bu$F  $       4F               while (*p && len < strlen(input)) {
 "N $        $ ^d%P  dF      $  .            .e   $     -c  "N$F  .$       4F                   if (*p >= 'a' && *p <= 'z') {
  #$$        $  $4*. "N.    zP  3r ..    ..  $c   *u     $  u$K$  4F       4L                       *p = *p - 32;
   ^N$e.     3  F$k*. "*C$$$# .z$" '$    4L  "$c. '#$eeedF  $$$9r JF       J$                   }
    $'"$$eu. 4  F3"K$ .e=*CB$$$$L .e$    '$bc.u$***hd6C""  4kF$4F $F     u@$F               len += 1;
    $   '"*$*@u N'L$B*"z*""     "$F" 4k 4c '7$"      "*$eu 4'L$J" $   .e$*"4F               p += 1;
    $      '"hC*$ "$#.P"          $me$"  #$*$       .  ^*INJL$"$  $e$$*#   4F           }               
    $         $b"h ".F     $"     ^F        $       9r   #L#$FJEd#C@"      4L
   .$         $Jb   J"..  4b      uF        *k      J%    #c^ $" d$        4L           ...
  :"$         $k9   $ $%4c $Bme.ze$         '*$+eee@*$"  :r$    @L$        4$
  $ $         $$Jr  $d" '$r "*==*"            "#**"" $r  4$3r  db$F        4F           char *args[] = { "/bin/bash", "-c", "--", message, NULL };
  $c$         $'*F  $"   '$            /\            $    *(L  $$$F         k           char *envp[] = { "PATH=:", NULL };
  #i*e.       $ 4>  $  ue $         \`.||.'/         'L c  $$ .L$d         .$           
   "b."*e.    4 4   $  $%db=eL     `.<\||/>.'      e*+$/$r  $ '$"$       .d$$           ...
    $^#+cC*mu 4r4   4r:6@F  $$    -----++-----    <$. "N?N  F  $ $    ud$$* $           
    $    "*eJ"@L4   4k*3Ic.*"      .'</||\>`.      #*5.J$$..F  $ $ ue#2*"   $           ret = execve("/bin/bash", args, envp);
    $       "N."@r  4Fd" '$r        /.'||`.\        4$ '"N*d"  9.$#Ce*"     $           
    $         "e^"  'd" uz$%           \/           '$czr"k#"  4Pu@"        $           ...

        WELCOME STRANGER! ONLY REAL NINJA ARE ALLOWED TO ENTER...

> 
```


## .instructions

```bash
# build container
sudo docker build -t jailbash .

# run container
sudo docker run --read-only 4000:4000 -d --restart=always jailbash

# connect
nc 127.0.0.1 4000
```

## .solution

As lowercase letters are converted to uppercase, use octal representation `$'\XYZ'`.