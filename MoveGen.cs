using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;




namespace Chess
{
    class MoveGen
    {
        public static List<int> GetMoves(int[] board, int pos)
        {

            int row = Board.GetRowCol(pos)[0];
            int col = Board.GetRowCol(pos)[1];

            int[] player;
            int[] opponent;
            if (Board.white.Contains(board[pos]))
            {
                player = Board.white;
                opponent = Board.black;
            }
            else if (Board.black.Contains(board[pos]))
            {
                player = Board.black;
                opponent = Board.white;
            }
            else
            {
                return null;
            }

            if (Board.pawn.Contains(board[pos]))
            {
                return PawnMoves(board, pos, row, col, opponent);
            }
            else if (Board.rook.Contains(board[pos]))
            {
                return RookMoves(board, row, col, opponent);
            }
            else if (Board.bishop.Contains(board[pos]))
            {
                return BishopMoves(board, row, col, opponent);
            }
            else if (Board.queen.Contains(board[pos]))
            {
                return QueenMoves(board, row, col, opponent);
            }
            else if (Board.king.Contains(board[pos]))
            {
                return KingMoves(board, row, col, opponent);
            }
            else if (Board.knight.Contains(board[pos]))
            {
                return KnightMoves(board, row, col, opponent);
            }
            else
            {
                return null;
            }
        }


        // TODO: Pawn turn into Queen
        public static List<int> PawnMoves(int[] board, int pos, int row, int col, int[] opponent)
        {
            List<int> moves = new List<int>();

            if (Board.white.Contains(board[pos]))
            {
                if (board[pos + 8] == 0)
                {
                    moves.Add(pos + 8);
                    if (row == 1 && board[pos + 16] == 0)
                    {
                        moves.Add(pos + 16);
                    }
                }
                if (col != 7 && opponent.Contains(board[Board.GetPos(row + 1, col + 1)]))
                {
                    moves.Add(Board.GetPos(row + 1, col + 1));
                }
                if (col != 0 && opponent.Contains(board[Board.GetPos(row + 1, col - 1)]))
                {
                    moves.Add(Board.GetPos(row + 1, col - 1));
                }
            }
            if (Board.black.Contains(board[pos]))
            {
                if (board[pos - 8] == 0)
                {
                    moves.Add(pos - 8);
                    if (row == 6 && board[pos - 16] == 0)
                    {
                        moves.Add(pos - 16);
                    }
                }
                if (col != 7 && opponent.Contains(board[Board.GetPos(row - 1, col + 1)]))
                {
                    moves.Add(Board.GetPos(row - 1, col + 1));
                }
                if (col != 0 && opponent.Contains(board[Board.GetPos(row - 1, col - 1)]))
                {
                    moves.Add(Board.GetPos(row - 1, col - 1));
                }
            }

            return moves;
        }


        public static List<int> RookMoves(int[] board, int row, int col, int[] opponent)
        {
            List<int> moves = new List<int>();

            int up = row - 1;
            int down = row + 1;
            int right = col + 1;
            int left = col - 1;

            while (up >= 0)
            {
                if (board[Board.GetPos(up, col)] != 0)
                {
                    if (opponent.Contains(board[Board.GetPos(up, col)]))
                    {
                        moves.Add(Board.GetPos(up, col));
                    }
                    break;
                }
                moves.Add(Board.GetPos(up, col));
                up -= 1;
            }
            while (down <= 7)
            {
                if (board[Board.GetPos(down, col)] != 0)
                {
                    if (opponent.Contains(board[Board.GetPos(down, col)]))
                    {
                        moves.Add(Board.GetPos(down, col));
                    }
                    break;
                }
                moves.Add(Board.GetPos(down, col));
                down += 1;
            }
            while (right <= 7)
            {
                if (board[Board.GetPos(row, right)] != 0)
                {
                    if (opponent.Contains(board[Board.GetPos(row, right)]))
                    {
                        moves.Add(Board.GetPos(row, right));
                    }
                    break;
                }
                moves.Add(Board.GetPos(row, right));
                right += 1;
            }
            while (left >= 0)
            {
                if (board[Board.GetPos(row, left)] != 0)
                {
                    if (opponent.Contains(board[Board.GetPos(row, left)]))
                    {
                        moves.Add(Board.GetPos(row, left));
                    }
                    break;
                }
                moves.Add(Board.GetPos(row, left));
                left -= 1;
            }

            return moves;

        }

        public static List<int> BishopMoves(int[] board, int row, int col, int[] opponent)
        {
            List<int> moves = new List<int>();

            int up = row - 1;
            int down = row + 1;
            int right = col + 1;
            int left = col - 1;
            bool moveRight = true;
            bool moveLeft = true;

            while (up >= 0)
            {
                if (right <= 7 && moveRight)
                {
                    if (board[Board.GetPos(up, right)] != 0)
                    {
                        if (opponent.Contains(board[Board.GetPos(up, right)]))
                        {
                            moves.Add(Board.GetPos(up, right));
                        }
                        moveRight = false;
                    }
                    if (moveRight)
                    {
                        moves.Add(Board.GetPos(up, right));
                    }
                }
                if (left >= 0 && moveLeft)
                {
                    if (board[Board.GetPos(up, left)] != 0)
                    {
                        if (opponent.Contains(board[Board.GetPos(up, left)]))
                        {
                            moves.Add(Board.GetPos(up, left));
                        }
                        moveLeft = false;
                    }
                    if (moveLeft)
                    {
                        moves.Add(Board.GetPos(up, left));
                    }
                }
                up -= 1;
                right += 1;
                left -= 1;
            }

            right = col + 1;
            left = col - 1;
            moveRight = true;
            moveLeft = true;
            while (down <= 7)
            {
                if (right <=7 && moveRight)
                {
                    if (board[Board.GetPos(down, right)] != 0)
                    {
                        if (opponent.Contains(board[Board.GetPos(down, right)]))
                        {
                            moves.Add(Board.GetPos(down, right));
                        }
                        moveRight = false;
                    }
                    if (moveRight)
                    {
                        moves.Add(Board.GetPos(down, right));
                    }
                }
                if (left >= 0 && moveLeft)
                {
                    if (board[Board.GetPos(down, left)] != 0)
                    {
                        if (opponent.Contains(board[Board.GetPos(down, left)]))
                        {
                            moves.Add(Board.GetPos(down, left));
                        }
                        moveLeft = false;
                    }
                    if (moveLeft)
                    {
                        moves.Add(Board.GetPos(down, left));
                    }
                }
                down += 1;
                right += 1;
                left -= 1;
            }

            return moves;
        }

        public static List<int> QueenMoves(int[] board, int row, int col, int[] opponent)
        {
            return RookMoves(board, row, col, opponent).Concat(BishopMoves(board, row, col, opponent)).ToList();
        }

        public static List<int> KingMoves(int[] board,int row, int col, int[] opponent)
        {
            List<int> moves = new List<int>();

            Tuple<int, int>[] coordinates = new Tuple<int, int>[8] { Tuple.Create(1, -1), Tuple.Create(1, 0), Tuple.Create(1, 1), Tuple.Create(0, -1), Tuple.Create(0, 1), Tuple.Create(-1, -1), Tuple.Create(-1, 0), Tuple.Create(-1, 1) };

            foreach (Tuple<int, int> move in coordinates)
            {
                int y = row + move.Item1;
                int x = col + move.Item2;
                if (y >= 0 && y <= 7 && x >= 0 && x <= 7 && (board[Board.GetPos(y, x)] == 0 || opponent.Contains(board[Board.GetPos(y, x)])))
                {
                    moves.Add(Board.GetPos(y, x));
                }
            }

            return moves;
        }

        public static List<int> KnightMoves(int[] board, int row, int col, int[] opponent)
        {
            List<int> moves = new List<int>();

            Tuple<int, int>[] coordinates = new Tuple<int, int>[8] { Tuple.Create(2, -1), Tuple.Create(2, 1), Tuple.Create(1, -2), Tuple.Create(1, 2), Tuple.Create(-1, -2), Tuple.Create(-1, 2), Tuple.Create(-2, -1), Tuple.Create(-2, 1) };

            foreach (Tuple<int, int> move in coordinates)
            {
                int y = row + move.Item1;
                int x = col + move.Item2;
                if (y >= 0 && y <= 7 && x >= 0 && x <= 7 && (board[Board.GetPos(y, x)] == 0 || opponent.Contains(board[Board.GetPos(y, x)])))
                {
                    moves.Add(Board.GetPos(y, x));
                }
            }

            return moves;
        }

        public static List<int[]> AllMoves(int[] board, int[] player)
        {
            List<int[]> moves = new List<int[]>();

            for (int pos = 0; pos < 64; pos++)
            {
                if (player.Contains(board[pos]))
                {
                    foreach (int newPos in GetMoves(board, pos))
                    {
                        int[] move = new int[2] { pos, newPos };
                        moves.Add(move);
                    }
                }
            }

            return moves;
        }

        public static int[] MakeMoveCopy(int[] board, int pos, int newPos)
        {
            int[] newBoard = board;
            //newBoard = board;
            return MakeMove(newBoard, pos, newPos);
            
        }

        public static int[] MakeMove(int[] board, int pos, int newPos)
        {
            int val = board[pos];
            board[pos] = 0;
            board[newPos] = val;

            return board;
        }






    }


}
