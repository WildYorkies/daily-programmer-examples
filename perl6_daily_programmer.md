

#[2016-06-01] Challenge #269 [Intermediate] Mirror encryption
	https://www.reddit.com/r/dailyprogrammer/comments/4m3ddb/20160601_challenge_269_intermediate_mirror/

No Solutions in Perl6

#[2016-09-16] Challenge #283 [Hard] Guarding the Coast
	https://www.reddit.com/r/dailyprogrammer/comments/5320ey/20160916_challenge_283_hard_guarding_the_coast/

No Solutions in Perl6

#[2016-05-20] Challenge #267 [Hard] IDDQD
	https://www.reddit.com/r/dailyprogrammer/comments/4k8m02/20160520_challenge_267_hard_iddqd/

No Solutions in Perl6

#[2016-12-15] Challenge #295 [Intermediate] Seperated Spouses
	https://www.reddit.com/r/dailyprogrammer/comments/5ijb4z/20161215_challenge_295_intermediate_seperated/

No Solutions in Perl6

#[2016-11-02] Challenge #290 [Intermediate] Blinking LEDs
	https://www.reddit.com/r/dailyprogrammer/comments/5as91q/20161102_challenge_290_intermediate_blinking_leds/

No Solutions in Perl6

#[2016-08-24] Challenge #280 [Intermediate] Anagram Maker
	https://www.reddit.com/r/dailyprogrammer/comments/4zcly2/20160824_challenge_280_intermediate_anagram_maker/

No Solutions in Perl6

#[2016-12-22] Challenge #296 [Intermediate] Intersecting Area Of Overlapping Rectangles
	https://www.reddit.com/r/dailyprogrammer/comments/5jpt8v/20161222_challenge_296_intermediate_intersecting/

No Solutions in Perl6

#[2016-07-29] Challenge #277 [Hard] Trippy Julia fractals
	https://www.reddit.com/r/dailyprogrammer/comments/4v5h3u/20160729_challenge_277_hard_trippy_julia_fractals/

No Solutions in Perl6

#[2016-08-16] Challenge #279 [Easy] Uuencoding
	https://www.reddit.com/r/dailyprogrammer/comments/4xy6i1/20160816_challenge_279_easy_uuencoding/

No Solutions in Perl6

#[2016-10-17] Challenge #288 [Easy] Detecting Alliteration
	https://www.reddit.com/r/dailyprogrammer/comments/57zcbm/20161017_challenge_288_easy_detecting_alliteration/

No Solutions in Perl6

#Challenge #270 [Easy] Transpose the input text
	https://www.reddit.com/r/dailyprogrammer/comments/4msu2x/challenge_270_easy_transpose_the_input_text/

No Solutions in Perl6

#[2016-08-08] Challenge #278 [Easy/Med] Weave insert Part 1
	https://www.reddit.com/r/dailyprogrammer/comments/4wqzph/20160808_challenge_278_easymed_weave_insert_part_1/

No Solutions in Perl6

#[2016-07-06] Challenge #274 [Intermediate] Calculating De Bruijn sequences
	https://www.reddit.com/r/dailyprogrammer/comments/4riubi/20160706_challenge_274_intermediate_calculating/

No Solutions in Perl6

#[2016-09-28] Challenge #285 [Intermediate] Cross Platform/Language Data Encoding part 2
	https://www.reddit.com/r/dailyprogrammer/comments/54wihd/20160928_challenge_285_intermediate_cross/

No Solutions in Perl6

#[2016-10-28] Challenge #289 [Hard] "Spot it!" cards generator
	https://www.reddit.com/r/dailyprogrammer/comments/59vml0/20161028_challenge_289_hard_spot_it_cards/

No Solutions in Perl6

#[2016-11-04] Challenge #290 [Hard] Gophers and Robot Dogs
	https://www.reddit.com/r/dailyprogrammer/comments/5b5fc8/20161104_challenge_290_hard_gophers_and_robot_dogs/

No Solutions in Perl6

#[2016-07-13] Challenge #275 [Intermediate] Splurthian Chemistry 102
	https://www.reddit.com/r/dailyprogrammer/comments/4so25w/20160713_challenge_275_intermediate_splurthian/

No Solutions in Perl6

#[2016-10-10] Challenge #287 [Easy] Kaprekar's Routine
	https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/

No Solutions in Perl6

#[2016-11-11] Challenge #291 [Hard] Spaghetti Wiring
	https://www.reddit.com/r/dailyprogrammer/comments/5cetzo/20161111_challenge_291_hard_spaghetti_wiring/

No Solutions in Perl6

#[2016-07-15] Challenge #275 [Hard] Splurthian Chemistry 103
	https://www.reddit.com/r/dailyprogrammer/comments/4t11c3/20160715_challenge_275_hard_splurthian_chemistry/

No Solutions in Perl6

#[2016-12-30] Challenge #297 [Hard] Parentheses trees
	https://www.reddit.com/r/dailyprogrammer/comments/5l42dx/20161230_challenge_297_hard_parentheses_trees/

##https://www.reddit.com/r/dailyprogrammer/comments/5l42dx/20161230_challenge_297_hard_parentheses_trees/dbx2qqx
Perl 6 with bonus 1:

    use v6;                                                                                 
                                                                                            
    sub MAIN(Bool :$reverse = False) {                                                      
        say $reverse ?? tree-to-string($_.EVAL) !! string-to-tree($_).perl for $*IN.lines;  
    }                                                                                       
                                                                                            
    grammar Grammar {                                                                       
        token expr { <term=word>* %% [ '(' ~ ')' <term=expr> ] }                            
        token word { <[\w\h]>* }                                                            
    }                                                                                       
                                                                                            
    class Actions {                                                                         
        method expr($/) { make $<term>».made }                                              
        method word($/) { make ~$/ }                                                        
    }                                                                                       
                                                                                            
    sub string-to-tree($s) {                                                                
        Grammar.parse($s, :rule<expr>, :actions(Actions.new)).made;                         
    }                                                                                       
                                                                                            
    sub tree-to-string($t) {                                                                
        ($t.map: { $_ ~~ Array ?? '(' ~ tree-to-string($_.list) ~ ')' !! ~$_ }).join;    
    }                                                                                       
                                                                                            
Note: Yes, EVAL is evil and it should never be applied to input from stdin... except in toy examples :)

#[2016-06-17] Challenge #271 [Hard] Formatting J code
	https://www.reddit.com/r/dailyprogrammer/comments/4ojbgq/20160617_challenge_271_hard_formatting_j_code/

No Solutions in Perl6

#[2016-07-27] Challenge #277 [Intermediate] Fake coins
	https://www.reddit.com/r/dailyprogrammer/comments/4utlaz/20160727_challenge_277_intermediate_fake_coins/

No Solutions in Perl6

#[2016-12-05] Challenge #294 [Easy] Rack management 1
	https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/

##https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/db46k5i
My solution in **Perl 6**, + bonus 1 and bonus 2

    use v6;

    multi MAIN (Str $tile where *.chars <= 20) {
        my $res = '';
        for 'enable1.txt'.IO.lines -> $word {
            next if $res.chars > $word.chars;
            last if $res.chars == $tile.chars; 
            $res = $word if word_exists($tile, $word); 
        }
        say "word found " ~ $res;

    }

    multi sub MAIN(Str $tile where $tile.chars == 7 , Str $word where $word.chars <= 7) {
        say $word, word_exists($tile, $word) ?? " found" !! " not found", " in '$tile'";

    }

    sub word_exists(Str $tile, Str $word) returns Bool {
        my @letters = $tile.comb;
        my Str $res = "";
        for $word.comb -> $w {
            my Int $i = @letters.first: $w, :k;
            $i = @letters.first: '?', :k unless defined $i;;
            next unless defined $i;
            $res = $res ~ @letters[$i];	
            @letters = map @letters.keys : { @letters[$_] if $_ != $i }
        }
        return  $res.chars == $word.chars;
    }

#[Meta] June 2016 Review
	https://www.reddit.com/r/dailyprogrammer/comments/4nglg5/meta_june_2016_review/

No Solutions in Perl6

#[2016-06-20] Challenge #272 [Easy] What's in the bag?
	https://www.reddit.com/r/dailyprogrammer/comments/4oylbo/20160620_challenge_272_easy_whats_in_the_bag/

No Solutions in Perl6

#[2017-02-03] Challenge #301 [Hard] Guitar Tablature
	https://www.reddit.com/r/dailyprogrammer/comments/5rt1cj/20170203_challenge_301_hard_guitar_tablature/

No Solutions in Perl6

#[2016-11-15] Challenge #292 [Easy] Increasing range parsing
	https://www.reddit.com/r/dailyprogrammer/comments/5d1l7v/20161115_challenge_292_easy_increasing_range/

No Solutions in Perl6

#[2016-07-25] Challenge #277 [Easy] Simplifying fractions
	https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/

##https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/d5yru16
**Perl6** with bonus

Solution shows using built-in Rat (rational) type, built-in gcd function, and a custom gcd function. Use of multi subs allows cleanup of if statements.

    sub MAIN(Bool :$bonus) {
        if (!$bonus) {
            loop {
                my ($a, $b) = prompt('').split(' ');

                say-join built-in-rat($a, $b);
                say-join with-gcd($a, $b, &infix:<gcd>);
                say-join with-gcd($a, $b, &my-gcd);
            }
        } else {
            my %subs;
            loop {
                my @in = prompt('').split(' ');
                say-join($_) with bonus(|@in, %subs);
            }
        }
    }

    sub built-in-rat($a, $b) { (+$a / +$b).nude; }

    sub with-gcd($a, $b, &gcd-fun) {
        my $gcd = &gcd-fun(+$a,+$b);
        (+$a / $gcd, +$b / $gcd);
    }

    multi sub my-gcd($a, 0) { $a }
    multi sub my-gcd($a, $b) { my-gcd($b, $a mod $b) }

    multi sub bonus($n, %subs) {
        %subs{*}:delete;
        for ^+$n {
            my ($a, $b) = prompt('').split(' ');
            %subs{$a} = apply($b, %subs);
        }
    }
    multi sub bonus($a, $b, %subs) {
        my $sub-a = apply($a, %subs);
        my $sub-b = apply($b, %subs);

        for $sub-a.comb -> $char {
            if defined $sub-a.index($char) and defined $sub-b.index($char) {
                $sub-a .= subst($char, '', :nth(1));
                $sub-b .= subst($char, '', :nth(1));
            }
        }
        ($sub-a || '1', $sub-b || '1')
    }

    sub say-join(@a) { say @a.join(' ') }

    sub apply($a, %subs) {
        ($a, |%subs.kv).reduce: { $^a.subst($^b, $^c, :g) };
    }

#[2016-07-22] Challenge #276 [Hard] ∞ Loop solver part 2
	https://www.reddit.com/r/dailyprogrammer/comments/4u3e96/20160722_challenge_276_hard_loop_solver_part_2/

No Solutions in Perl6

#[2016-10-05] Challenge #286 [Intermediate] Zeckendorf Representations of Positive Integers
	https://www.reddit.com/r/dailyprogrammer/comments/55zdxx/20161005_challenge_286_intermediate_zeckendorf/

No Solutions in Perl6

#[2016-09-05] Challenge #282 [Easy] Unusual Bases
	https://www.reddit.com/r/dailyprogrammer/comments/5196fi/20160905_challenge_282_easy_unusual_bases/

No Solutions in Perl6

#[2016-11-07] Challenge #291 [Easy] Goldilocks' Bear Necessities
	https://www.reddit.com/r/dailyprogrammer/comments/5bn0b7/20161107_challenge_291_easy_goldilocks_bear/

No Solutions in Perl6

#[2016-07-20] Challenge #276 [Intermediate] Key function
	https://www.reddit.com/r/dailyprogrammer/comments/4tqy5c/20160720_challenge_276_intermediate_key_function/

##https://www.reddit.com/r/dailyprogrammer/comments/4tqy5c/20160720_challenge_276_intermediate_key_function/d5jx2ao
**Perl6**

    sub key(@src, @key, &f) {
        my %data;
        my %agg;
        for (@key Z @src) -> ($k, $v) {
            if !(%agg{$k}:exists) {
                %agg{$k} = %agg.elems;
            }
            %data{$k}.push($v);
        }
        return %data.pairs.map({[$^a.key, &f($^a.value)]}).sort: { %agg{$^a[0]} };
    }

    sub print_keys(@v, @k, &f) {
        for key(@v, @k, &f) -> $e {
            say "$e[0] $e[1]";
        }
    }

    sub tabular($file, &f) {
        my (@k, @v);
        for $file.IO.slurp.comb(/\S+/).rotor(2) -> ($k, $v) {
            @k.push($k);
            @v.push($v);
        }
        print_keys(@v, @k, &f);
    }

    multi MAIN('histogram', $file) {
        my @v = $file.IO.comb(/\S+/);
        print_keys(@v, @v, *.elems);
    }

    multi MAIN('sum', $file) {
        tabular($file, &sum);
    }

    multi MAIN('nub', $file) {
        tabular($file, *[0]);
    }


##https://www.reddit.com/r/dailyprogrammer/comments/4tqy5c/20160720_challenge_276_intermediate_key_function/d5jx7d8
The 3 mains mean you get this sort of behavior:

    $ perl6 key.p6
    Usage:
      key.p6 histogram <file>
      key.p6 sum <file>
      key.p6 nub <file>
    $ perl6 key.p6 histogram hist.txt
    5 13
    3 12
    2 8
    9 14
    7 8



#[2016-09-26] Challenge #285 [Easy] Cross Platform/Language Data Encoding part 1
	https://www.reddit.com/r/dailyprogrammer/comments/54lu54/20160926_challenge_285_easy_cross/

No Solutions in Perl6

#[2016-06-08] Challenge #270 [Intermediate] Generating Text with Markov Processes
	https://www.reddit.com/r/dailyprogrammer/comments/4n6hc2/20160608_challenge_270_intermediate_generating/

##https://www.reddit.com/r/dailyprogrammer/comments/4n6hc2/20160608_challenge_270_intermediate_generating/d44dk7m
Not surprised or even sad to see no Perl here. But Perl 6, now that's a different story. I have only been at it for a few days, but I am already completely head over heels, and one would really be unwise to dismiss it on grounds of its historical linkage with the predecessor.

(One caveat: it's *painfully* slow now. But it will be faster...someday. And then it will fix the world)

    my $text = slurp.lc.subst(/<[\S] - [a..z]>/, "", :g).words;

    my %next;
    for $text.rotor(3 => -2) -> ($a, $b, $c) { %next{ "{$a}+{$b}" }{ $c }++; }

    my ($first, $second) = %next.pick.key.split("+");
    my @chain = $first, $second, -> $a, $b { %next{ "{$a}+{$b}" }.roll.key } ... *;
    say @chain[^1000].join(" ");
 

#[2017-01-04] Challenge #298 [Intermediate] Too many or too few Parentheses
	https://www.reddit.com/r/dailyprogrammer/comments/5m034l/20170104_challenge_298_intermediate_too_many_or/

No Solutions in Perl6

#[2017-01-09] Challenge #298 [Hard] Functional Maze solving
	https://www.reddit.com/r/dailyprogrammer/comments/5mzr6x/20170109_challenge_298_hard_functional_maze/

No Solutions in Perl6

#[2016-05-23] Challenge #268 [Easy] Network and Cards: Part 1, The network
	https://www.reddit.com/r/dailyprogrammer/comments/4knivr/20160523_challenge_268_easy_network_and_cards/

No Solutions in Perl6

#[2016-08-29] Challenge #281 [Easy] Something about bases
	https://www.reddit.com/r/dailyprogrammer/comments/504rdh/20160829_challenge_281_easy_something_about_bases/

No Solutions in Perl6

#[2017-01-23] Challenge #300 [Easy] Let's make some noise
	https://www.reddit.com/r/dailyprogrammer/comments/5prdgb/20170123_challenge_300_easy_lets_make_some_noise/

No Solutions in Perl6

#[2016-08-18] Challenge #279 [Intermediate] Text Reflow
	https://www.reddit.com/r/dailyprogrammer/comments/4ybbcz/20160818_challenge_279_intermediate_text_reflow/

No Solutions in Perl6

#[2016-10-21] Challenge #288 [Hard] Adjacent Numbers problems
	https://www.reddit.com/r/dailyprogrammer/comments/58n2ca/20161021_challenge_288_hard_adjacent_numbers/

No Solutions in Perl6

#[2016-09-09] Challenge #282 [Hard] Hidato
	https://www.reddit.com/r/dailyprogrammer/comments/51wg0j/20160909_challenge_282_hard_hidato/

No Solutions in Perl6

#[2016-09-30] Challenge #285 [Hard] Math Proofs
	https://www.reddit.com/r/dailyprogrammer/comments/557wyy/20160930_challenge_285_hard_math_proofs/

No Solutions in Perl6

#[2016-11-24] Challenge #293 [Intermediate] Defusing the second bomb
	https://www.reddit.com/r/dailyprogrammer/comments/5emuuy/20161124_challenge_293_intermediate_defusing_the/

No Solutions in Perl6

#[2016-06-24] Challenge #272 [Hard] Air Pressure router valve - Part 1.
	https://www.reddit.com/r/dailyprogrammer/comments/4pnky5/20160624_challenge_272_hard_air_pressure_router/

No Solutions in Perl6

#[2016-06-10] Challenge #270 [Hard] Alien Invasion Inversion
	https://www.reddit.com/r/dailyprogrammer/comments/4nga90/20160610_challenge_270_hard_alien_invasion/

No Solutions in Perl6

#[2016-07-01] Challenge #273 [Hard] Elggob - Make a Boggle Layout
	https://www.reddit.com/r/dailyprogrammer/comments/4qt12j/20160701_challenge_273_hard_elggob_make_a_boggle/

No Solutions in Perl6

#[2016-11-25] Challenge #293 [Hard] Zombies 2 - Your Princess is in Another Castle!
	https://www.reddit.com/r/dailyprogrammer/comments/5etds6/20161125_challenge_293_hard_zombies_2_your/

No Solutions in Perl6

#[2016-09-23] Challenge #284 [Hard] Winning the Tournament
	https://www.reddit.com/r/dailyprogrammer/comments/545a7x/20160923_challenge_284_hard_winning_the_tournament/

No Solutions in Perl6

#[2016-12-23] Challenge #296 [Hard] Flood Fill Puzzle Game
	https://www.reddit.com/r/dailyprogrammer/comments/5jxeal/20161223_challenge_296_hard_flood_fill_puzzle_game/

No Solutions in Perl6

#[2016-10-07] Challenge #286 [Hard] Rush Hour Solver
	https://www.reddit.com/r/dailyprogrammer/comments/56bh88/20161007_challenge_286_hard_rush_hour_solver/

No Solutions in Perl6

#[2016-05-27] Challenge #268 [Hard] Network and Cards: Part 3, The cheaters
	https://www.reddit.com/r/dailyprogrammer/comments/4lavv6/20160527_challenge_268_hard_network_and_cards/

No Solutions in Perl6

#[2017-02-10] Challenge #302 [Hard] ASCII Histogram Maker: Part 2 - The Proper Histogram
	https://www.reddit.com/r/dailyprogrammer/comments/5t7l07/20170210_challenge_302_hard_ascii_histogram_maker/

No Solutions in Perl6

#[2016-09-07] Challenge #282 [Intermediate] The final Quixo move
	https://www.reddit.com/r/dailyprogrammer/comments/51l1j1/20160907_challenge_282_intermediate_the_final/

No Solutions in Perl6

#[2016-07-18] Challenge #276 [Easy] Recktangles
	https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/

##https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/d5h693i
**Perl6** no bonus

    sub rect($word, $len, $w, $h) {
        for 0 .. $len * $w -> $x {
            for 0 .. $len * $h -> $y {
                if !($x % $len) || !($y % $len) {
                    my $ind = ($x + $y) % $word.chars;
                    print $word.substr($ind, 1);
                }
                else {
                    print ' ';
                }
            }
            say "";
        }
    }

    sub MAIN($word, Int $w, Int $h) {
        # Creates source string from word: rect => rectce
        my $str = $word ~ $word.substr(1, $word.chars -2).flip;
        rect($str, $word.chars - 1, $w, $h);
    }


##https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/d5hcde4
**Bonus Hex**

    sub hex($word, $len, $w, $h) {
        my $diag = $word.chars + $len;
        for (0 .. $word.chars * $h) >>%>> $word.chars -> $y {
            print '    .';
            for (0 .. $word.chars * $w + $len) -> $x {
                my $xmod = $x % $word.chars;
                my $off = $x div $word.chars % 2 * $len;
                my $ymod = ($y + $off) % $word.chars;
                if ($ymod - $xmod == $len || $ymod + $xmod == $len)
                    || ($ymod == 0 && $xmod >= $len) {
                    my $ind = ($x + $len) % $word.chars;
                    print $word.substr($ind, 1);
                }
                else {
                    print ' ';
                }
            }
            say "";
        }
    }

    sub MAIN($word, Int $w, Int $h) {
        # Creates source string from word: rect => rectce
        my $str = $word ~ $word.substr(1, $word.chars -2).flip;
        hex($str, $word.chars - 1, $w, $h);
    }

perl6 hex.p6 rect 2 2

    .   rect        r
    .  e    c      e 
    . c      e    c  
    .t        rect   
    . c      e    c  
    .  e    c      e 
    .   rect        r
    .  e    c      e 
    . c      e    c  
    .t        rect   
    . c      e    c  
    .  e    c      e 
    .   rect        r

##https://www.reddit.com/r/dailyprogrammer/comments/4tetif/20160718_challenge_276_easy_recktangles/d5h8j2u
**Bonus diamonds**

    sub diamond($word, $len, $w, $h) {
        for 0 .. $len * 2 * $w -> $x {
            for 0 .. $len * 2 * $h -> $y {
                if ($x + $y) % $word.chars == $len || abs($x - $y) % $word.chars == $len {
                    my $ind = $x % $word.chars;
                    print $word.substr($ind, 1);
                }
                else {
                    print ' ';
                }
            }
            say "";
        }
    }
    sub MAIN($word, Int $w, Int $h) {
        # Creates source string from word: rect => rectce
        my $str = $word ~ $word.substr(1, $word.chars -2).flip;
        diamond($str, $word.chars - 1, $w, $h);
    }

perl6 diamonds.p6 shiny 2 3
 
    # I have to lead with . so the formatting works, otherwise, it looks terrible
    .    s       s       s    
    .   h h     h h     h h   
    .  i   i   i   i   i   i  
    . n     n n     n n     n 
    .y       y       y       y
    . n     n n     n n     n 
    .  i   i   i   i   i   i  
    .   h h     h h     h h   
    .    s       s       s    
    .   h h     h h     h h   
    .  i   i   i   i   i   i  
    . n     n n     n n     n 
    .y       y       y       y
    . n     n n     n n     n 
    .  i   i   i   i   i   i  
    .   h h     h h     h h   
    .    s       s       s    



#[2016-07-04] Challenge #274 [Easy] Gold and Treasure: The Beale Cipher
	https://www.reddit.com/r/dailyprogrammer/comments/4r8fod/20160704_challenge_274_easy_gold_and_treasure_the/

No Solutions in Perl6

#[2016-10-31] Challenge #290 [Easy] Kaprekar Numbers
	https://www.reddit.com/r/dailyprogrammer/comments/5aemnn/20161031_challenge_290_easy_kaprekar_numbers/

No Solutions in Perl6

#[2016-12-16] Challenge #295 [Hard] Advanced pacman
	https://www.reddit.com/r/dailyprogrammer/comments/5iq4ix/20161216_challenge_295_hard_advanced_pacman/

No Solutions in Perl6

#[2016-06-13] Challenge #271 [Easy] Critical Hit
	https://www.reddit.com/r/dailyprogrammer/comments/4nvrnx/20160613_challenge_271_easy_critical_hit/

No Solutions in Perl6

#[PSA] [Monthly Challenge #11 - October, 2016] - Procedural Ghosts and Jack-o-Lanterns! • /r/proceduralgeneration
	https://www.reddit.com/r/proceduralgeneration/comments/55xkud/monthly_challenge_11_october_2016_procedural/

No Solutions in Perl6

#[2016-08-26] Challenge #280 [Hard] Free Flow Solver
	https://www.reddit.com/r/dailyprogrammer/comments/4zog32/20160826_challenge_280_hard_free_flow_solver/

No Solutions in Perl6

#Weekly #26 - Mini Challenges
	https://www.reddit.com/r/dailyprogrammer/comments/56mfgz/weekly_26_mini_challenges/

##https://www.reddit.com/r/dailyprogrammer/comments/56mfgz/weekly_26_mini_challenges/dbqy5a7
A little engineered to learn the language more.

    #!/usr/bin/env perl6
    
    use v6;
    
    subset ValidFile of Str where {
      .IO ~~ :f or warn "Input file doesn't exist."
    }
    
    multi MAIN(Str $cmd) {
      simple_xargs($*IN, $cmd);
    }
    
    multi MAIN(ValidFile $file, Str $cmd) {
      simple_xargs($file.IO, $cmd);
    }
    
    sub simple_xargs($input, $cmd) {
      $input.lines.map: ->$line {
        run $cmd, $line
      }
    }

Couple of cool things:

- Multiple dispatch on MAIN gives a simple way to design CLI. Providing no argument even prints a nice usage message (which can be overridden with your own `sub USAGE`).
- Subset of a type to restrict it further. This can make the logic a bit free of clutter.

#[2016-12-19] Challenge #296 [Easy] The Twelve Days of...
	https://www.reddit.com/r/dailyprogrammer/comments/5j6ggm/20161219_challenge_296_easy_the_twelve_days_of/

##https://www.reddit.com/r/dailyprogrammer/comments/5j6ggm/20161219_challenge_296_easy_the_twelve_days_of/dbk0hrx
My solution in *Perl 6*, with bonus 1 and 2

    use v6;

    my @days = < first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth>;
    my @numbers = < a two three four five six seven eight nine ten eleven twelve>;
    my @gifts = 'input.txt'.IO.lines;

    for [0 .. @days.end] -> $i {
        say "On the " ~ @days[$i] ~ " day of Christmas";
        say "my true love sent to me: ";
        if $i == 0 {
            say @numbers[0] ~ @gifts[0] 
        }
        else {
            for [0..$i].reverse -> $j {
                say "and " ~ @numbers[$j] ~ " " ~ @gifts[$j] and next if $j == 0;
                say @numbers[$j]~ " " ~ @gifts[$j]; 
            }
        }
        say "\n";		
    }



#[2016-10-24] Challenge #289 [Easy] It's super effective!
	https://www.reddit.com/r/dailyprogrammer/comments/5961a5/20161024_challenge_289_easy_its_super_effective/

No Solutions in Perl6

#[2016-10-14] Challenge #287 [Hard] Word Numbers
	https://www.reddit.com/r/dailyprogrammer/comments/57fzcv/20161014_challenge_287_hard_word_numbers/

No Solutions in Perl6

#[2016-10-03] Challenge #286 [Easy] Reverse Factorial
	https://www.reddit.com/r/dailyprogrammer/comments/55nior/20161003_challenge_286_easy_reverse_factorial/

No Solutions in Perl6

#[2016-06-29] Challenge #273 [Intermediate] Twist up a message
	https://www.reddit.com/r/dailyprogrammer/comments/4qg2eo/20160629_challenge_273_intermediate_twist_up_a/

No Solutions in Perl6

#[2016-09-02] Challenge #281 [Hard] Minesweeper Solver
	https://www.reddit.com/r/dailyprogrammer/comments/50s3ax/20160902_challenge_281_hard_minesweeper_solver/

No Solutions in Perl6

#[2016-11-09] Challenge #291 [Intermediate] Reverse Polish Notation Calculator
	https://www.reddit.com/r/dailyprogrammer/comments/5c5jx9/20161109_challenge_291_intermediate_reverse/

No Solutions in Perl6

#[Weekly #25] Escape the trolls
	https://www.reddit.com/r/dailyprogrammer/comments/4vrb8n/weekly_25_escape_the_trolls/

No Solutions in Perl6

#[2016-05-25] Challenge #268 [Intermediate] Network and Cards: Part 2, The cards
	https://www.reddit.com/r/dailyprogrammer/comments/4kz0e0/20160525_challenge_268_intermediate_network_and/

No Solutions in Perl6

#[2017-01-26] Challenge #300 [Easy/Intermediate] Let's make some noise part 2
	https://www.reddit.com/r/dailyprogrammer/comments/5q9cll/20170126_challenge_300_easyintermediate_lets_make/

No Solutions in Perl6

#[2017-02-08] Challenge #302 [Intermediate] ASCII Histogram Maker: Part 1 - The Simple Bar Chart
	https://www.reddit.com/r/dailyprogrammer/comments/5st2so/20170208_challenge_302_intermediate_ascii/

No Solutions in Perl6

#[2017-01-13] Challenge #299 [Hard] Functional Graph solving
	https://www.reddit.com/r/dailyprogrammer/comments/5nr86m/20170113_challenge_299_hard_functional_graph/

No Solutions in Perl6

#[2016-10-12] Challenge #287 [Intermediate] Mathagrams
	https://www.reddit.com/r/dailyprogrammer/comments/576o8o/20161012_challenge_287_intermediate_mathagrams/

No Solutions in Perl6

#[2016-11-21] Challenge #293 [Easy] Defusing the bomb
	https://www.reddit.com/r/dailyprogrammer/comments/5e4mde/20161121_challenge_293_easy_defusing_the_bomb/

No Solutions in Perl6

#[2017-02-02] Challenge #301 [Easy/Intemerdiate] Looking for patterns
	https://www.reddit.com/r/dailyprogrammer/comments/5rlpz1/20170202_challenge_301_easyintemerdiate_looking/

##https://www.reddit.com/r/dailyprogrammer/comments/5rlpz1/20170202_challenge_301_easyintemerdiate_looking/dd8fd2i
Cheaty solution (Perl 6):

    sub MAIN(Str $pattern is copy) {
      $pattern.comb.unique.kv.map: -> $index, $char {
        $pattern .= subst( / $char /, "(\\w)" );
        $pattern .= subst( / $char /, "\$$index", :g);
      }
      "/usr/share/dict/words".IO.lines.grep(/<$pattern>/)>>.say;
    }


#[2016-09-12] Challenge #283 [Easy] Anagram Detector
	https://www.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/

##https://www.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/d7jrseu
**Perl6**

    sub as-bag($s) {
        # Get a count of each lower-cased letter (\w) in the string
        # Bag is basically a hash of key => count, plus lots of useful methods
        return $s.lc.comb(/\w/).Bag;
    }
    for lines() -> $l {
        # Perl6's regex is a bit different than perl5.  In this case specifically:
        # [^chars] becomes <-[ chars ]>
        # The /x flag (whitespace in regex) is on by default
        # All literal strings are quoted instead of bare
        if $l ~~ /'"' (<-["]> +) '" ? "' (<-[ " ]> +) '"'/ {
            if as-bag($0) ~~ as-bag($1) {
                say qq["$0" is an anagram of "$1"];
            }
            else {
                say qq["$0" is NOT an anagram of "$1"];
            }
        }
    }


##https://www.reddit.com/r/dailyprogrammer/comments/52enht/20160912_challenge_283_easy_anagram_detector/d7n14lw
Perl6

    for $input.lines.flatmap: *.split(/ \s+ \? \s+ /) -> Str $first, Str $second {
        $first.lc.comb(/\w/).sort ~~ $second.lc.comb(/\w/).sort
            ?? say $first ~ " is an anagram of "     ~ $second
    	    !! say $first ~ " is NOT an anagram of " ~ $second;
    }

#[2016-09-21] Challenge #284 [Intermediate] Punch Card Creator
	https://www.reddit.com/r/dailyprogrammer/comments/53sw7z/20160921_challenge_284_intermediate_punch_card/

No Solutions in Perl6

#[2017-02-06] Challenge #302 [Easy] Spelling with Chemistry
	https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/

##https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/ddezgqo
Perl 6 with bonus. This language is full of tricks.

    my %periodic_table = "./pt-data2.csv".IO.lines.map: {
      my $data = $_.split(/","/);
      $data[1].trim => ($data[2].trim,
                        $data[3].comb(/<[\d]+[\.]>+/).[0]);
    }
    
    my $elements = "[{%periodic_table.keys>>.lc.join("|")}]";
    slurp.lines.map: {
      $_ ~~ m:ex/^ (<$elements>)+ $/;
      my $sorted = ($/.flat.sort: {
        [+] gather for $_.flat { take %periodic_table{~$_.tc}[1]; }
      }).reverse.[0];
      say "{$sorted[0]>>.tc.join} ({(%periodic_table{~$_.tc}[0] for $sorted.flat).join(" ")})";
    }


#[2017-01-2] Challenge #298 [Easy] Too many Parentheses
	https://www.reddit.com/r/dailyprogrammer/comments/5llkbj/2017012_challenge_298_easy_too_many_parentheses/

No Solutions in Perl6

#[2016-06-22] Challenge #272 [Intermediate] Dither that image
	https://www.reddit.com/r/dailyprogrammer/comments/4paxp4/20160622_challenge_272_intermediate_dither_that/

No Solutions in Perl6

#[2016-10-19] Challenge #288 [Intermediate] Stars and Stripes and Vertices
	https://www.reddit.com/r/dailyprogrammer/comments/589txl/20161019_challenge_288_intermediate_stars_and/

No Solutions in Perl6

#[2016-09-19] Challenge #284 [Easy] Wandering Fingers
	https://www.reddit.com/r/dailyprogrammer/comments/53ijnb/20160919_challenge_284_easy_wandering_fingers/

##https://www.reddit.com/r/dailyprogrammer/comments/53ijnb/20160919_challenge_284_easy_wandering_fingers/d7y7cis
perl6

    sub MAIN (Str $input) {
        my @chars = $input.comb;
        
        my %dict = ('a' .. 'z').map: * => (('a' .. 'z').map: * => []).hash;
    
        for 'example.txt'.IO.lines».comb -> @chars {
    	%dict{ @chars.head }{ @chars.tail }.push: @chars[ 1 .. * - 2 ];
        }
    
        for |%dict{ @chars.head }{ @chars.tail } -> @solution {
    	say (@chars.head, |@solution, @chars.tail).join if is_valid(@solution, @chars[ 1 .. *-1 ]);
        }
    }
    
    sub is_valid(@solution, @chars is copy) {
        return False if @chars < @solution;
        my Int $i = 0;
        for @solution -> Str $s {
    	$i = (@chars.first: * eq $s, :k) // return False;
    	@chars = @chars[ $i .. *-1 ];
        }
        return True;
    }


#[2016-06-15] Challenge #271 [Intermediate] Making Waves
	https://www.reddit.com/r/dailyprogrammer/comments/4o74p3/20160615_challenge_271_intermediate_making_waves/

##https://www.reddit.com/r/dailyprogrammer/comments/4o74p3/20160615_challenge_271_intermediate_making_waves/d4atlfs
**Perl6** solution, no bonus

    #Running program with bad arguments produces:
    #Usage:
    #  sound.p6 [-w=<Str>] [-o=<Str>] <filename>
    sub MAIN(Str $filename, Str :$w='sine', Str :$o) {
        my $file = $filename ?? open $filename !! $*IN;
        my $sample_rate = $file.get.Int;
        my $duration = $file.get.Int;

        # Avaliable waveforms
        my %waveform = (
            sine => sub { (sin($^a * 2 * pi)) * 127 + 128},
            square => sub { $^a < .5 ?? 255 !! 0 },
            triangle => sub { (($^a * 510) - 255).abs },
            sawtooth => sub { $^a * 255 },
        );

        my $wave = %waveform{$w};
        unless $wave {
            say "Invalid waveform: $w";
            say "Valid options are: $(%waveform.keys)";
            exit(1);
        }

        # Set output to STDOUT, or the file passed in
        my $out = $o ?? open($o, :bin, :w) !! $*OUT;

        # * can be used as the argument to an anonymous function
        # Convert frequencies to map of increase per sample
        my %freq = 'ABCDEFG_'.comb Z=> (440, 493.88, 523.25, 587.33, 659.25, 698.46, 783.99, 0).map: */$sample_rate;
        my $window = 0;
        my $wave_point = 0;
        my $t = 1000/$sample_rate;
        for $file.comb(/<[A .. G _]>/) -> $note {
            my $step = %freq{$note};
            while $window < $duration {
                $out.write(Buf.new($wave($wave_point).Int));
                $window += $t;
                $wave_point = ($wave_point + $step) % 1;
            }
            $window %= $duration;
        }
    }


#[ANN] Only one challenge this week
	https://www.reddit.com/r/dailyprogrammer/comments/4vr831/ann_only_one_challenge_this_week/

No Solutions in Perl6

#[2016-06-27] Challenge #273 [Easy] Getting a degree
	https://www.reddit.com/r/dailyprogrammer/comments/4q35ip/20160627_challenge_273_easy_getting_a_degree/

No Solutions in Perl6

#[2016-12-09] Challenge #294 [Hard] Rack management 3
	https://www.reddit.com/r/dailyprogrammer/comments/5hcd0x/20161209_challenge_294_hard_rack_management_3/

No Solutions in Perl6

#[2017-01-11] Challenge #299 [Intermediate] From Maze to graph
	https://www.reddit.com/r/dailyprogrammer/comments/5nciz5/20170111_challenge_299_intermediate_from_maze_to/

No Solutions in Perl6

#[2016-12-07] Challenge #294 [Intermediate] Rack management 2
	https://www.reddit.com/r/dailyprogrammer/comments/5h40ml/20161207_challenge_294_intermediate_rack/

No Solutions in Perl6

#[2016-08-22] Challenge #280 [Easy] 0 to 100, Real Quick
	https://www.reddit.com/r/dailyprogrammer/comments/4z04vj/20160822_challenge_280_easy_0_to_100_real_quick/

No Solutions in Perl6

#[2017-01-28] Challenge #300 [Hard] Let's make some noise part 3
	https://www.reddit.com/r/dailyprogrammer/comments/5qp3ou/20170128_challenge_300_hard_lets_make_some_noise/

No Solutions in Perl6

#[2016-12-12] Challenge #295 [Easy] Letter by letter
	https://www.reddit.com/r/dailyprogrammer/comments/5hy8sm/20161212_challenge_295_easy_letter_by_letter/

##https://www.reddit.com/r/dailyprogrammer/comments/5hy8sm/20161212_challenge_295_easy_letter_by_letter/db5gnpk
My solution in **Perl 6**:

    use v6;
    
    sub MAIN(Str $input1, Str $input2 where *.chars == $input1.chars) {
	    say $input1;
	    my @a = $input1.comb;
	    my @b = $input2.comb;
	    for  @a.keys -> $i {
		    @a[$i] = @b[$i] and say @a.join('') if @b[$i] ne @a[$i];
	    }
    }


#[2016-08-31] Challenge #281 [Intermediate] Dank usernames
	https://www.reddit.com/r/dailyprogrammer/comments/50hbtp/20160831_challenge_281_intermediate_dank_usernames/

No Solutions in Perl6

#[2016-10-27] Challenge #289 [Intermediate] Metro trip planner
	https://www.reddit.com/r/dailyprogrammer/comments/59mnxa/20161027_challenge_289_intermediate_metro_trip/

No Solutions in Perl6

#[2016-07-11] Challenge #275 [Easy] Splurthian Chemistry 101
	https://www.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/

No Solutions in Perl6

#[2016-07-08] Challenge #274 [Hard] ∞ Loop solver
	https://www.reddit.com/r/dailyprogrammer/comments/4rug59/20160708_challenge_274_hard_loop_solver/

No Solutions in Perl6

#[2016-05-30] Challenge #269 [Easy] BASIC Formatting
	https://www.reddit.com/r/dailyprogrammer/comments/4lpygb/20160530_challenge_269_easy_basic_formatting/

No Solutions in Perl6