(set-info :smt-lib-version 2.6)
(set-logic QF_LIA)
(set-info :info "only one Boolean model, and we should block such instances")
(set-info :category "random")
(set-info :status sat)
(declare-fun x0 () Int)
(declare-fun x1 () Int)
(declare-fun x2 () Int)
(declare-fun x3 () Int)
(declare-fun x4 () Int)
(declare-fun x5 () Int)
(declare-fun x6 () Int)
(declare-fun x7 () Int)
(declare-fun x8 () Int)
(declare-fun x9 () Int)

(assert (and 
(<= (- 9) (+ (* (- 2) x0) (+ (* (- 2) x1) (+ (* 2 x2) (+ (* (- 2) x3) (+ (* (- 1) x5) (+ (* 1 x6) (* (- 2) x7) ))))))) 
(<= (- 10) (+ (* (- 2) x0) (+ (* (- 2) x1) (+ (* 1 x2) (+ (* 1 x3) (+ (* 1 x4) (+ (* 2 x5) (+ (* 2 x8) (* (- 1) x9) )))))))) 
(<= 17 (+ (* (- 1) x0) (+ (* (- 1) x1) (+ (* 2 x5) (+ (* (- 1) x6) (+ (* 1 x7) (+ (* (- 2) x8) (* (- 2) x9) ))))))) 
(<= 5 (+ (* 1 x2) (+ (* (- 1) x3) (+ (* 2 x4) (+ (* 1 x5) (+ (* (- 2) x6) (+ (* (- 1) x8) (* 2 x9) ))))))) 
(<= 10 (+ (* 1 x1) (+ (* (- 1) x3) (+ (* (- 1) x4) (* (- 2) x8) )))) 
(<= 4 (+ (* (- 1) x0) (+ (* 2 x3) (+ (* (- 1) x4) (+ (* (- 1) x5) (* (- 2) x8) ))))) 
(<= 2 (+ (* 2 x0) (+ (* 1 x1) (+ (* (- 1) x2) (+ (* (- 1) x3) (+ (* (- 2) x4) (+ (* 1 x6) (+ (* (- 1) x7) (* (- 1) x9) )))))))) 
(<= 9 (+ (* 1 x1) (+ (* (- 1) x6) (+ (* 1 x7) (+ (* (- 2) x8) (* 2 x9) ))))) 
(<= (- 4) (+ (* 2 x2) (+ (* (- 2) x3) (+ (* (- 1) x4) (+ (* (- 1) x7) (* 2 x8) ))))) 
(<= (- 23) (+ (* 7 x0) (+ (* 3 x1) (+ (* (- 7) x2) (+ (* 4 x3) (+ (* 7 x4) (+ (* (- 2) x6) (+ (* 7 x7) (+ (* 7 x8) (* 2 x9) ))))))))) 
(<= (- 119) (+ (* (- 12) x0) (+ (* (- 11) x1) (+ (* 12 x2) (+ (* (- 5) x3) (+ (* (- 1) x4) (+ (* (- 5) x5) (+ (* 10 x6) (+ (* (- 16) x7) (+ (* 11 x8) (* (- 1) x9) )))))))))) 
(<= 45 (+ (* (- 16) x0) (+ (* (- 5) x1) (+ (* 13 x2) (+ (* (- 3) x3) (+ (* (- 6) x4) (+ (* 6 x5) (+ (* (- 1) x6) (+ (* (- 8) x7) (* (- 13) x8) ))))))))) 
(<= (- 82) (+ (* (- 10) x0) (+ (* (- 9) x1) (+ (* 9 x2) (+ (* (- 8) x3) (+ (* (- 19) x4) (+ (* (- 15) x5) (+ (* 20 x6) (+ (* (- 21) x7) (+ (* 3 x8) (* (- 12) x9) )))))))))) 
(<= (- 41) (+ (* 15 x0) (+ (* 4 x1) (+ (* (- 19) x2) (+ (* 13 x3) (+ (* 12 x4) (+ (* (- 5) x5) (+ (* (- 1) x6) (+ (* 12 x7) (+ (* 8 x8) (* (- 1) x9) )))))))))) 
(<= 135 (+ (* 30 x0) (+ (* 16 x1) (+ (* (- 22) x2) (+ (* 3 x3) (+ (* 4 x4) (+ (* 3 x5) (+ (* (- 14) x6) (+ (* 21 x7) (+ (* (- 7) x8) (* 3 x9) ))))))))))))
(check-sat)
(exit)