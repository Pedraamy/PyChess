import pygame

from .cvars import *



class Place:

    def __init__(self, pos):
        self.pos = pos
        self.pos_x = None
        self.pos_y = None


    def pos_n(self):
        self.pos = (self.pos[0] - 1, self.pos[1])

    def pos_s(self):
        self.pos = (self.pos[0] + 1, self.pos[1])

    def pos_e(self):
        self.pos = (self.pos[0], self.pos[1] - 1)

    def pos_w(self):
        self.pos = (self.pos[0], self.pos[1] + 1)

    def pos_ne(self):
        self.pos = (self.pos[0] - 1, self.pos[1] - 1)

    def pos_nw(self):
        self.pos = (self.pos[0] - 1, self.pos[1] + 1)

    def pos_se(self):
        self.pos = (self.pos[0] + 1, self.pos[1] - 1)

    def pos_sw(self):
        self.pos = (self.pos[0] + 1, self.pos[1] + 1)

    def calc_pos(self):
        self.pos_x = (self.pos[1] * SQ_SIZE) + 15
        self.pos_y = (self.pos[0] * SQ_SIZE) + 10



class Piece(Place):

    def __init__(self, pos, color):
        super().__init__(pos)
        self.color = color
        self.moved = False
        self.moves_list = []
        if color == "black":
            self.min_range = -50
            self.max_range = 0
        else:
            self.min_range = 0
            self.max_range = 50


    def draw_piece(self):
        self.calc_pos()
        WINDOW.blit(self.imgur, (self.pos_x, self.pos_y))
    

    def blit_moves(self):
        self.calc_pos()
        pygame.draw.circle(WINDOW, BLACK, (self.pos_x + 35, self.pos_y + 40), 47, width = 1)
        self.valid_moves()
        for move in self.moves_list:
            circler = Place(move)
            circler.calc_pos()
            pygame.draw.circle(WINDOW, GREEN, (circler.pos_x + 34, circler.pos_y + 38), 7)



class Knight(Piece):
    value = 3
    
    def __init__(self, pos, color):
        super().__init__(pos, color)
        if color == "black":
            self.value = Knight.value * -1
            self.imgur = bKNIGHT
        else:
            self.value = Knight.value
            self.imgur = wKNIGHT
    

    def valid_moves(self):
        self.moves_list = []

        #NNE
        move_check = Place(self.pos)
        move_check.pos_n()
        move_check.pos_ne()
        check = move_check.pos
        if check[0] in range(8) and check[1] in range(8):
            if not self.min_range < Board.piece_dict[check] < self.max_range:
                self.moves_list.append(check)

        #NNW
        move_check = Place(self.pos)
        move_check.pos_n()
        move_check.pos_nw()
        check = move_check.pos
        if check[0] in range(8) and check[1] in range(8):
            if not self.min_range < Board.piece_dict[check] < self.max_range:
                self.moves_list.append(check)

        #WNW
        move_check = Place(self.pos)
        move_check.pos_w()
        move_check.pos_nw()
        check = move_check.pos
        if check[0] in range(8) and check[1] in range(8):
            if not self.min_range < Board.piece_dict[check] < self.max_range:
                self.moves_list.append(check)

        #WSW
        move_check = Place(self.pos)
        move_check.pos_w()
        move_check.pos_sw()
        check = move_check.pos
        if check[0] in range(8) and check[1] in range(8):
            if not self.min_range < Board.piece_dict[check] < self.max_range:
                self.moves_list.append(check)

        #SSW
        move_check = Place(self.pos)
        move_check.pos_s()
        move_check.pos_sw()
        check = move_check.pos
        if check[0] in range(8) and check[1] in range(8):
            if not self.min_range < Board.piece_dict[check] < self.max_range:
                self.moves_list.append(check)

        #SSE
        move_check = Place(self.pos)
        move_check.pos_s()
        move_check.pos_se()
        check = move_check.pos
        if check[0] in range(8) and check[1] in range(8):
            if not self.min_range < Board.piece_dict[check] < self.max_range:
                self.moves_list.append(check)

        #ESE
        move_check = Place(self.pos)
        move_check.pos_e()
        move_check.pos_se()
        check = move_check.pos
        if check[0] in range(8) and check[1] in range(8):
            if not self.min_range < Board.piece_dict[check] < self.max_range:
                self.moves_list.append(check)

        #ENE
        move_check = Place(self.pos)
        move_check.pos_e()
        move_check.pos_ne()
        check = move_check.pos
        if check[0] in range(8) and check[1] in range(8):
            if not self.min_range < Board.piece_dict[check] < self.max_range:
                self.moves_list.append(check)



class Bishop(Piece):
    value = 3

    def __init__(self, pos, color):
        super().__init__(pos, color)
        if color == "black":
            self.value = Bishop.value * -1
            self.imgur = bBISHOP
        else:
            self.value = Bishop.value
            self.imgur = wBISHOP
    

    def valid_moves(self):
        self.moves_list = []

        #NW
        move_check = Place(self.pos)
        move_check.pos_nw()
        check = move_check.pos
        while check[0] >= 0 and check[1] <= 7:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_nw()
            check = move_check.pos

        #NE
        move_check = Place(self.pos)
        move_check.pos_ne()
        check = move_check.pos
        while check[0] >= 0 and check[1] >= 0:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_ne()
            check = move_check.pos

        #SW
        move_check = Place(self.pos)
        move_check.pos_sw()
        check = move_check.pos
        while check[0] <= 7 and check[1] <= 7:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_sw()
            check = move_check.pos

        #SE
        move_check = Place(self.pos)
        move_check.pos_se()
        check = move_check.pos
        while check[0] <= 7 and check[1] >= 0:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_se()
            check = move_check.pos
        


class Rook(Piece):
    value = 5

    def __init__(self, pos, color):
        super().__init__(pos, color)
        if color == "black":
            self.value = Rook.value * -1
            self.imgur = bROOK
        else:
            self.value = Rook.value
            self.imgur = wROOK


    def valid_moves(self):
        self.moves_list = []

        #N
        move_check = Place(self.pos)
        move_check.pos_n()
        check = move_check.pos
        while check[0] >= 0:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_n()
            check = move_check.pos

        #S
        move_check = Place(self.pos)
        move_check.pos_s()
        check = move_check.pos
        while check[0] <= 7:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_s()
            check = move_check.pos

        #E
        move_check = Place(self.pos)
        move_check.pos_e()
        check = move_check.pos
        while check[1] >= 0:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_e()
            check = move_check.pos

        #W
        move_check = Place(self.pos)
        move_check.pos_w()
        check = move_check.pos
        while check[1] <= 7:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_w()
            check = move_check.pos
        


class Pawn(Piece):
    value = 1

    def __init__(self, pos, color):
        super().__init__(pos, color)
        if color == "black":
            self.value = Pawn.value * -1
            self.imgur = bPAWN
        else:
            self.value = Pawn.value
            self.imgur = wPAWN
        self.passant = False
    

    def valid_moves(self):
        self.moves_list = []

        if self.color == "white":
            #N
            move_check = Place(self.pos)
            move_check.pos_n()
            check = move_check.pos
            if check[0] in range(8):
                if Board.piece_dict[check] == 0:
                    self.moves_list.append(check)
                    if self.moved == False:
                        move_check.pos_n()
                        check = move_check.pos
                        if Board.piece_dict[check] == 0:
                            self.moves_list.append(check)

            #CNE
            move_check = Place(self.pos)
            move_check.pos_ne()
            check = move_check.pos
            if check[0] in range(8) and check[1] in range(8):
                if Board.piece_dict[check] < 0:
                    self.moves_list.append(check)

            #CNW
            move_check = Place(self.pos)
            move_check.pos_nw()
            check = move_check.pos
            if check[0] in range(8) and check[1] in range(8):
                if Board.piece_dict[check] < 0:
                    self.moves_list.append(check)

            #EN PASSANT
            checker_e = Place(self.pos)
            checker_w = Place(self.pos)
            checker_e.pos_e()
            check_east = checker_e.pos
            checker_w.pos_w()
            check_west = checker_w.pos
            for piece in Board.pieces_master:
                if piece.pos == check_east:
                    if piece.color != self.color:
                        if isinstance(piece, Pawn):
                            if piece.passant == True:
                                checker_e.pos_n()
                                add_passant = checker_e.pos
                                self.moves_list.append(add_passant)
                                Board.passant_squares.append(add_passant)

            for piece in Board.pieces_master:
                if piece.pos == check_west:
                    if piece.color != self.color:
                        if isinstance(piece, Pawn):
                            if piece.passant == True:
                                checker_w.pos_n()
                                add_passant = checker_w.pos
                                self.moves_list.append(add_passant)
                                Board.passant_squares.append(add_passant)

        else:
            #S
            move_check = Place(self.pos)
            move_check.pos_s()
            check = move_check.pos
            if check[0] in range(8):
                if Board.piece_dict[check] == 0:
                    self.moves_list.append(check)
                    if self.moved == False:
                        move_check.pos_s()
                        check = move_check.pos
                        if Board.piece_dict[check] == 0:
                            self.moves_list.append(check)

            #CSE
            move_check = Place(self.pos)
            move_check.pos_se()
            check = move_check.pos
            if check[0] in range(8) and check[1] in range(8):
                if Board.piece_dict[check] > 0:
                    self.moves_list.append(check)

            #CSW
            move_check = Place(self.pos)
            move_check.pos_sw()
            check = move_check.pos
            if check[0] in range(8) and check[1] in range(8):
                if Board.piece_dict[check] > 0:
                    self.moves_list.append(check)

            #EN PASSANT
            checker_e = Place(self.pos)
            checker_w = Place(self.pos)
            checker_e.pos_e()
            check_east = checker_e.pos
            checker_w.pos_w()
            check_west = checker_w.pos
            for piece in Board.pieces_master:
                if piece.pos == check_east:
                    if piece.color != self.color:
                        if isinstance(piece, Pawn):
                            if piece.passant == True:
                                checker_e.pos_s()
                                add_passant = checker_e.pos
                                self.moves_list.append(add_passant)
                                Board.passant_squares.append(add_passant)

            for piece in Board.pieces_master:
                if piece.pos == check_west:
                    if piece.color != self.color:
                        if isinstance(piece, Pawn):
                            if piece.passant == True:
                                checker_w.pos_s()
                                add_passant = checker_w.pos
                                self.moves_list.append(add_passant)
                                Board.passant_squares.append(add_passant)
        

class Queen(Piece):
    value = 9

    def __init__(self, pos, color):
        super().__init__(pos, color)
        if color == "black":
            self.value = Queen.value * -1
            self.imgur = bQUEEN
        else:
            self.value = Queen.value
            self.imgur = wQUEEN


    def valid_moves(self):
        self.moves_list = []

        #NW
        move_check = Place(self.pos)
        move_check.pos_nw()
        check = move_check.pos
        while check[0] >= 0 and check[1] <= 7:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_nw()
            check = move_check.pos

        #NE
        move_check = Place(self.pos)
        move_check.pos_ne()
        check = move_check.pos
        while check[0] >= 0 and check[1] >= 0:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_ne()
            check = move_check.pos

        #SW
        move_check = Place(self.pos)
        move_check.pos_sw()
        check = move_check.pos
        while check[0] <= 7 and check[1] <= 7:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_sw()
            check = move_check.pos

        #SE
        move_check = Place(self.pos)
        move_check.pos_se()
        check = move_check.pos
        while check[0] <= 7 and check[1] >= 0:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_se()
            check = move_check.pos

        #N
        move_check = Place(self.pos)
        move_check.pos_n()
        check = move_check.pos
        while check[0] >= 0:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_n()
            check = move_check.pos

        #S
        move_check = Place(self.pos)
        move_check.pos_s()
        check = move_check.pos
        while check[0] <= 7:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_s()
            check = move_check.pos

        #E
        move_check = Place(self.pos)
        move_check.pos_e()
        check = move_check.pos
        while check[1] >= 0:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_e()
            check = move_check.pos

        #W
        move_check = Place(self.pos)
        move_check.pos_w()
        check = move_check.pos
        while check[1] <= 7:
            if Board.piece_dict[check] == 0:
                self.moves_list.append(check)
            elif self.min_range < Board.piece_dict[check] < self.max_range:
                break
            else:
                self.moves_list.append(check)
                break
            move_check.pos_w()
            check = move_check.pos



class King(Piece):
    value = 22

    def __init__(self, pos, color):
        super().__init__(pos, color)
        if color == "black":
            self.value = King.value * -1
            self.imgur = bKING
        else:
            self.value = King.value
            self.imgur = wKING


    def valid_moves(self):
        self.moves_list = []

        #N
        move_check = Place(self.pos)
        move_check.pos_n()
        check = move_check.pos
        if check[0] >= 0 and not self.min_range < Board.piece_dict[check] < self.max_range:
            self.moves_list.append(check)

        #S
        move_check = Place(self.pos)
        move_check.pos_s()
        check = move_check.pos
        if check[0] <= 7 and not self.min_range < Board.piece_dict[check] < self.max_range:
            self.moves_list.append(check)

        #E
        move_check = Place(self.pos)
        move_check.pos_e()
        check = move_check.pos
        if check[1] >= 0 and not self.min_range < Board.piece_dict[check] < self.max_range:
            self.moves_list.append(check)

        #W
        move_check = Place(self.pos)
        move_check.pos_w()
        check = move_check.pos
        if check[1] <= 7 and not self.min_range < Board.piece_dict[check] < self.max_range:
            self.moves_list.append(check)

        #NW
        move_check = Place(self.pos)
        move_check.pos_nw()
        check = move_check.pos
        if check[0] >= 0 and check[1] <= 7 and not self.min_range < Board.piece_dict[check] < self.max_range:
            self.moves_list.append(check)

        #NE
        move_check = Place(self.pos)
        move_check.pos_ne()
        check = move_check.pos
        if check[0] >= 0 and check[1] >= 0 and not self.min_range < Board.piece_dict[check] < self.max_range:
            self.moves_list.append(check)

        #SW
        move_check = Place(self.pos)
        move_check.pos_sw()
        check = move_check.pos
        if check[0] <= 7 and check[1] <= 7 and not self.min_range < Board.piece_dict[check] < self.max_range:
            self.moves_list.append(check)

        #SE
        move_check = Place(self.pos)
        move_check.pos_se()
        check = move_check.pos
        if check[0] <= 7 and check[1] >= 0 and not self.min_range < Board.piece_dict[check] < self.max_range:
            self.moves_list.append(check)
    


class Board:
    pieces_master = []
    piece_dict = {}

    castle_squares = [(0, 2), (0, 6), (7, 2), (7, 6)]
    passant_squares = []


    def __init__(self):
        self.initialize_board()
        self.gen_piece_dict()
        self.start = True
        self.turn = "white"
        self.error = False
        self.selected = None
        self.last_origin = None
        self.last_new = None
        self.last_moved = None
        self.can_castle = False
        self.promote = False
        self.board_backup = []
        self.checkmate = False
        self.stalemate = False

    def update(self):
        self.draw_board()
        self.gen_piece_dict()
        self.board_pieces()
        if self.start == True:
            self.draw_start()
        if self.checkmate == True:
            self.draw_mate()
        if self.stalemate == True:
            self.draw_stalemate()
        if self.selected != None:
            self.selected.blit_moves()
            if self.can_castle == True:
                self.blit_castle()
        if self.error == True:
            self.draw_error()
        if self.promote == True:
            self.draw_promotion()
        pygame.display.update()


    def click(self, location):
        if self.start == True:
            self.start = False

        elif self.error == True:
            self.revert_pos()
            self.error = False
        
        elif self.promote == True:
            if location in [(3, 3), (3, 4), (4, 3), (4, 4)]:
                self.choose_promotion(location)
                self.promote = False
                self.finalize_turn()
            else:
                return None

        elif self.selected == None:
            piece = self.get_piece(location)
            if piece == None:
                return None
            elif piece.color != self.turn:
                return None
            else:
                self.selected = piece
                if isinstance(self.selected, King):
                    if self.kings_castle() == True or self.queens_castle() == True:
                        self.can_castle = True
                
        else:
            if self.can_castle == True and location in Board.castle_squares:
                self.castle(location)

            elif location in self.selected.moves_list:
                self.move_piece(self.selected.pos, location)
                
                self.finalize_turn()

            else:
                self.selected = None
                self.can_castle = False
    

    def finalize_turn(self):
        self.gen_piece_dict()
        opp_moves_check = self.opp_moves()
        king_check = self.return_king_pos()

        self.selected = None
        self.can_castle = False

        if self.check_for_check(king_check, opp_moves_check) == True:
            self.error = True
            return None
        
        if self.check_promotion() == True:
            self.promote = True
            return None

        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
        
        if self.check_checkmate() == True:
            opp_moves_check = self.opp_moves()
            king_check = self.return_king_pos()
            if self.check_for_check(king_check, opp_moves_check) == True:
                self.checkmate = True
            else:
                self.stalemate = True


    def move_piece(self, old, new):
        self.last_origin = old
        self.last_new = new

        self.board_backup = Board.pieces_master[:]
        if Board.piece_dict[new] != 0:
            self.remove_piece(new)
        elif new in Board.passant_squares and isinstance(self.selected, Pawn) == True:
            if self.turn == "white":
                remover = Place(new)
                remover.pos_s()
                self.remove_piece(remover.pos)
            else:
                remover = Place(new)
                remover.pos_n()
                self.remove_piece(remover.pos)

        for piece in Board.pieces_master:
            if piece.color == self.turn:
                if isinstance(piece, Pawn):
                    if piece.passant == True:
                        piece.passant = False
                        Board.passant_squares = []

        for piece in Board.pieces_master:
            if piece.pos == old:
                self.last_moved = piece.moved
                piece.pos = new
                if isinstance(piece, Pawn):
                    if abs(new[0] - old[0]) == 2:
                        piece.passant = True
                if piece.moved == False:
                    piece.moved = True

    
    def remove_piece(self, pos):
        for piece in Board.pieces_master:
            if piece.pos == pos:
                Board.pieces_master.remove(piece)
    

    def revert_pos(self):
        for piece in Board.pieces_master:
            if piece.pos == self.last_new:
                piece.pos = self.last_origin
                piece.moved = self.last_moved
        Board.pieces_master = self.board_backup[:]


    def get_piece(self, pos):
        for piece in Board.pieces_master:
            if piece.pos == pos:
                return piece
        return None
    

    def check_checkmate(self):
        for piece in Board.pieces_master:
            if piece.color == self.turn:
                start = piece.pos
                piece.valid_moves()
                for move in piece.moves_list:
                    self.move_piece(start, move)
                    self.gen_piece_dict()
                    mate_moves = self.opp_moves()
                    king_check = self.return_king_pos()
                    if self.check_for_check(king_check, mate_moves) == False:
                        self.revert_pos()
                        self.gen_piece_dict()
                        return False
                    else:
                        self.revert_pos()
                        self.gen_piece_dict()
        return True
    

    def check_for_check(self, king_pos, moves):
        if king_pos in moves:
            return True
        return False
    

    def opp_moves(self):
        opp_moves_l = []

        if self.turn == "black":
            for piece in Board.pieces_master:
                if piece.color == "white":
                    piece.valid_moves()
                    for move in piece.moves_list:
                        opp_moves_l.append(move)
        else:
            for piece in Board.pieces_master:
                if piece.color == "black":
                    piece.valid_moves()
                    for move in piece.moves_list:
                        opp_moves_l.append(move)
        return opp_moves_l
    

    def return_king_pos(self):
        if self.turn == "white":
            for piece in Board.pieces_master:
                if isinstance(piece, King):
                    if piece.color == "white":
                        return piece.pos
        else:
            for piece in Board.pieces_master:
                if isinstance(piece, King):
                    if piece.color == "black":
                        return piece.pos


    def check_promotion(self):
        for piece in Board.pieces_master:
            if piece.color == self.turn:
                if isinstance(piece, Pawn):
                    checker = piece.pos
                    if checker[0] == 0 or checker[0] == 7:
                        return True
        return False
    

    def choose_promotion(self, location):
        if self.turn == "white":
            for piece in Board.pieces_master:
                if piece.color == self.turn:
                    if isinstance(piece, Pawn):
                        checker = piece.pos[0]
                        if checker == 0:
                            placer = piece.pos
                            self.remove_piece(placer)
                            if location == (3, 3):
                                Board.pieces_master.append(Queen(placer, "white"))
                            elif location == (3, 4):
                                Board.pieces_master.append(Rook(placer, "white"))
                            elif location == (4, 3):
                                Board.pieces_master.append(Knight(placer, "white"))
                            else:
                                Board.pieces_master.append(Bishop(placer, "white"))

        else:
            for piece in Board.pieces_master:
                if piece.color == self.turn:
                    if isinstance(piece, Pawn):
                        checker = piece.pos[0]
                        if checker == 7:
                            placer = piece.pos
                            self.remove_piece(placer)
                            if location == (3, 3):
                                Board.pieces_master.append(Queen(placer, "black"))
                            elif location == (3, 4):
                                Board.pieces_master.append(Rook(placer, "black"))
                            elif location == (4, 3):
                                Board.pieces_master.append(Knight(placer, "black"))
                            else:
                                Board.pieces_master.append(Bishop(placer, "black"))
    

    def castle(self, spot):
        if spot[1] < 4:
            for piece in Board.pieces_master:
                if piece.pos == (spot[0], 4):
                    piece.pos = (spot[0], 2)
                if piece.pos == (spot[0], 0):
                    piece.pos = (spot[0], 3)

        else:
            for piece in Board.pieces_master:
                if piece.pos == (spot[0], 4):
                    piece.pos = (spot[0], 6)
                if piece.pos == (spot[0], 7):
                    piece.pos = (spot[0], 5)
            
        self.selected = None
        self.can_castle = False
        
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
        
        if self.check_checkmate() == True:
            opp_moves_check = self.opp_moves()
            king_check = self.return_king_pos()
            if self.check_for_check(king_check, opp_moves_check) == True:
                self.checkmate = True
            else:
                self.stalemate = True


    def kings_castle(self):
        checker = self.opp_moves()
        valid_rook = False
        if self.turn == "white":
            for piece in Board.pieces_master:
                if isinstance(piece, King):
                    if piece.color == "white":
                        if piece.moved == True:
                            return False
                if isinstance(piece, Rook):
                    if piece.color == "white":
                        if piece.pos == (7, 7):
                            if piece.moved == False:
                                valid_rook = True
            if valid_rook == False:
                return False
            if Board.piece_dict[(7, 5)] != 0 or Board.piece_dict[(7, 6)] != 0:
                return False
            if (7, 4) in checker or (7, 5) in checker or (7, 6) in checker:
                return False
            return True
        else:
            for piece in Board.pieces_master:
                if isinstance(piece, King):
                    if piece.color == "black":
                        if piece.moved == True:
                            return False
                if isinstance(piece, Rook):
                    if piece.color == "black":
                        if piece.pos == (0, 7):
                            if piece.moved == False:
                                valid_rook = True
            if valid_rook == False:
                return False
            if Board.piece_dict[(0, 5)] != 0 or Board.piece_dict[(0, 6)] != 0:
                return False
            if (0, 4) in checker or (0, 5) in checker or (0, 6) in checker:
                return False
            return True
        

    def queens_castle(self):
        checker = self.opp_moves()
        valid_rook = False
        if self.turn == "white":
            for piece in Board.pieces_master:
                if isinstance(piece, King):
                    if piece.color == "white":
                        if piece.moved == True:
                            return False
                if isinstance(piece, Rook):
                    if piece.color == "white":
                        if piece.pos == (7, 0):
                            if piece.moved == False:
                                valid_rook = True
            if valid_rook == False:
                return False
            if Board.piece_dict[(7, 3)] != 0 or Board.piece_dict[(7, 2)] != 0 or Board.piece_dict[(7, 1)] != 0:
                return False
            if (7, 4) in checker or (7, 3) in checker or (7, 2) in checker:
                return False
            return True

        else:
            for piece in Board.pieces_master:
                if isinstance(piece, King):
                    if piece.color == "black":
                        if piece.moved == True:
                            return False
                if isinstance(piece, Rook):
                    if piece.color == "black":
                        if piece.pos == (0, 0):
                            if piece.moved == False:
                                valid_rook = True
            if valid_rook == False:
                return False
            if Board.piece_dict[(0, 3)] != 0 or Board.piece_dict[(0, 2)] != 0 or Board.piece_dict[(0, 1)] != 0:
                return False
            if (0, 4) in checker or (0, 3) in checker or (0, 2) in checker:
                return False
            return True
    

    def blit_castle(self):
        if self.turn == "white":
            if self.kings_castle() == True:
                castler = Place((7, 6))
                castler.calc_pos()
                WINDOW.blit(castle_icon, (castler.pos_x + 25, castler.pos_y + 25))

            if self.queens_castle() == True:
                castler = Place((7, 2))
                castler.calc_pos()
                WINDOW.blit(castle_icon, (castler.pos_x + 25, castler.pos_y + 25))

        else:
            if self.kings_castle() == True:
                castler = Place((0, 6))
                castler.calc_pos()
                WINDOW.blit(castle_icon, (castler.pos_x + 25, castler.pos_y + 25))

            if self.queens_castle() == True:
                castler = Place((0, 2))
                castler.calc_pos()
                WINDOW.blit(castle_icon, (castler.pos_x + 25, castler.pos_y + 25))
    

    def draw_start(self):
        WINDOW.blit(start_CHESS, (225, 300))
        WINDOW.blit(start_FLASH, (122, 536))


    def draw_error(self):
        king_check = self.return_king_pos()
        for piece in Board.pieces_master:
            if piece.color != self.turn:
                piece.valid_moves()
                if king_check in piece.moves_list:
                    king_temp = Place(king_check)
                    king_temp.calc_pos()
                    piece.calc_pos()
                    pygame.draw.line(WINDOW, BLACK, (piece.pos_x + 30, piece.pos_y + 30), (king_temp.pos_x + 30, king_temp.pos_y + 30), 2)


    def draw_promotion(self):
        for row in range(3, 5):
            for col in range(3, 5):
                pygame.draw.rect(WINDOW, WHITE, (row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        
        pygame.draw.line(WINDOW, BLACK, (3 * SQ_SIZE, 3 * SQ_SIZE), (3 * SQ_SIZE, 5 * SQ_SIZE), 2)
        pygame.draw.line(WINDOW, BLACK, (4 * SQ_SIZE, 3 * SQ_SIZE), (4 * SQ_SIZE, 5 * SQ_SIZE), 2)
        pygame.draw.line(WINDOW, BLACK, (5 * SQ_SIZE, 3 * SQ_SIZE), (5 * SQ_SIZE, 5 * SQ_SIZE), 2)

        pygame.draw.line(WINDOW, BLACK, (3 * SQ_SIZE, 3 * SQ_SIZE), (5 * SQ_SIZE, 3 * SQ_SIZE), 2)
        pygame.draw.line(WINDOW, BLACK, (3 * SQ_SIZE, 4 * SQ_SIZE), (5 * SQ_SIZE, 4 * SQ_SIZE), 2)
        pygame.draw.line(WINDOW, BLACK, (3 * SQ_SIZE, 5 * SQ_SIZE), (5 * SQ_SIZE, 5 * SQ_SIZE), 2)

        queen = Place((3, 3))
        queen.calc_pos()
        WINDOW.blit(pro_QUEEN, (queen.pos_x, queen.pos_y))

        rook = Place((3, 4))
        rook.calc_pos()
        WINDOW.blit(pro_ROOK, (rook.pos_x, rook.pos_y))

        knight = Place((4, 3))
        knight.calc_pos()
        WINDOW.blit(pro_KNIGHT, (knight.pos_x, knight.pos_y))

        bishop = Place((4, 4))
        bishop.calc_pos()
        WINDOW.blit(pro_BISHOP, (bishop.pos_x, bishop.pos_y))

        WINDOW.blit(piece_SELECT, (100, 225))
    

    def draw_mate(self):
        if self.turn == "white":
            WINDOW.blit(red_MATE, (200, 300))
        else:
            WINDOW.blit(blue_MATE, (200, 300))

    
    def draw_stalemate(self):
        WINDOW.blit(stale_MATE, (200, 300))


    def gen_piece_dict(self):
        for row in range(8):
            for col in range(8):
                Board.piece_dict[(row, col)] = 0
        
        for piece in Board.pieces_master:
            Board.piece_dict[piece.pos] += piece.value


    def draw_board(self):
        WINDOW.fill(PURPLE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(WINDOW, BEIGE, (row * SQ_SIZE, col * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        

    def board_pieces(self):
        for piece in Board.pieces_master:
            piece.draw_piece()
            

    def initialize_board(self):
        Board.pieces_master.append(Pawn((6, 0), "white"))
        Board.pieces_master.append(Pawn((6, 1), "white"))
        Board.pieces_master.append(Pawn((6, 2), "white"))
        Board.pieces_master.append(Pawn((6, 3), "white"))
        Board.pieces_master.append(Pawn((6, 4), "white"))
        Board.pieces_master.append(Pawn((6, 5), "white"))
        Board.pieces_master.append(Pawn((6, 6), "white"))
        Board.pieces_master.append(Pawn((6, 7), "white"))

        Board.pieces_master.append(Pawn((1, 0), "black"))
        Board.pieces_master.append(Pawn((1, 1), "black"))
        Board.pieces_master.append(Pawn((1, 2), "black"))
        Board.pieces_master.append(Pawn((1, 3), "black"))
        Board.pieces_master.append(Pawn((1, 4), "black"))
        Board.pieces_master.append(Pawn((1, 5), "black"))
        Board.pieces_master.append(Pawn((1, 6), "black"))
        Board.pieces_master.append(Pawn((1, 7), "black"))

        Board.pieces_master.append(Rook((7, 0), "white"))
        Board.pieces_master.append(Rook((7, 7), "white"))

        Board.pieces_master.append(Rook((0, 0), "black"))
        Board.pieces_master.append(Rook((0, 7), "black"))

        Board.pieces_master.append(Knight((7, 1), "white"))
        Board.pieces_master.append(Knight((7, 6), "white"))

        Board.pieces_master.append(Knight((0, 1), "black"))
        Board.pieces_master.append(Knight((0, 6), "black"))

        Board.pieces_master.append(Bishop((7, 2), "white"))
        Board.pieces_master.append(Bishop((7, 5), "white"))

        Board.pieces_master.append(Bishop((0, 2), "black"))
        Board.pieces_master.append(Bishop((0, 5), "black"))

        Board.pieces_master.append(Queen((7, 3), "white"))
        Board.pieces_master.append(Queen((0, 3), "black"))

        Board.pieces_master.append(King((7, 4), "white"))
        Board.pieces_master.append(King((0, 4), "black"))



