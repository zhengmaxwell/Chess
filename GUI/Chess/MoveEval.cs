using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chess
{
    class MoveEval
    {
        public static int count = 0;
        public const int MAX_LEVEL = 1;


        public static Dictionary<int, int> values = new Dictionary<int, int>()
        {
            {10, 1 },
            {20, 1 },
            {11, 3 },
            {21, 3 },
            {12, 3 },
            {22, 3 },
            {13, 5 },
            {23, 5 },
            {14, 9 },
            {24, 9 },
            {15, 10000 },
            {25, 10000 }
        };

        public static double[] black_pawn = new double[64]   {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
                                                1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
                                                0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
                                                0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
                                                0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
                                                0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,
                                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };

        public static double[] white_pawn = new double[64]   {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5,
                                                0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5,
                                                0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0,
                                                0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5,
                                                1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0,
                                                5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
                                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};

        public static double[] all_knight = new double[64]   {-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
                                                -4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0,
                                                -3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0,
                                                -3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0,
                                                -3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0,
                                                -3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0,
                                                -4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0,
                                                -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0 };

        public static double[] black_bishop = new double[64] {-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
                                                -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
                                                -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
                                                -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
                                                -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
                                                -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
                                                -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
                                                -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0 };

        public static double[] white_bishop = new double[64]  {-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
                                                 -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0,
                                                 -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0,
                                                 -1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0,
                                                 -1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0,
                                                 -1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0,
                                                 -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
                                                 -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0 };

        public static double[] black_rook = new double[64]  {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                             0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
                                            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                            -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                             0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0 };

        public static double[] white_rook = new double[64]    {0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0,
                                                -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                                -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                                -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                                -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                                -0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5,
                                                0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
                                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 };

        public static double[] black_queen = new double[64] { -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
                                                -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
                                                -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
                                                -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
                                                 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
                                                -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
                                                -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
                                                -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0 };

        public static double[] white_queen = new double[64] {-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
                                                -1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0,
                                                -1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
                                                0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
                                                -0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5,
                                                -1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0,
                                                -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0,
                                                -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0 };

        public static double[] black_king = new double[64]    { -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                                                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                                                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                                                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                                                    -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
                                                    -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
                                                     2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
                                                     2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 };

        public static double[] white_king = new double[64] {2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0,
                                                2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0,
                                                -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
                                                -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
                                                -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                                                -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                                                -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                                                -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0 };


        public static double PosVal(int[] board, int pos)
        {
            if (Board.knight.Contains(board[pos]))
            {
                return all_knight[pos];
            }
            if (Board.white.Contains(board[pos]))
            {
                if (Board.pawn.Contains(board[pos]))
                {
                    return white_pawn[pos];
                }
                else if (Board.rook.Contains(board[pos]))
                {
                    return white_rook[pos];
                }
                else if (Board.bishop.Contains(board[pos]))
                {
                    return white_bishop[pos];
                }
                else if (Board.queen.Contains(board[pos]))
                {
                    return white_queen[pos];
                }
                else
                {
                    return white_king[pos];
                }
            }
            else
            {
                if (Board.pawn.Contains(board[pos]))
                {
                    return black_pawn[pos];
                }
                else if (Board.rook.Contains(board[pos]))
                {
                    return black_rook[pos];
                }
                else if (Board.bishop.Contains(board[pos]))
                {
                    return black_bishop[pos];
                }
                else if (Board.queen.Contains(board[pos]))
                {
                    return black_queen[pos];
                }
                else
                {
                    return black_king[pos];
                }
            }
        }


        public static double BoardVal(int[] board, int[] player)
        {
            double score = 0;

            for (int pos = 0; pos < 64; pos++)
            {
                if (board[pos] == 0)
                {
                    continue;
                }
                else if (player.Contains(board[pos]))
                {
                    score += values[board[pos]] + (PosVal(board, pos) / 10);
                }
                else
                {
                    score -= values[board[pos]] + (PosVal(board, pos) / 10);
                }
}
            return score;
        }


        public static double SmartBoardVal(int[] board, int[] player, double score, int[] move)
        {
            double newScore = score;
            int[] opposition = new int[6];
            if (Board.white == player)
            {
                opposition = Board.black;
            }
            else
            {
                opposition = Board.white;
            }

            double oldPos = PosVal(board, move[0]);
            int[] newBoard = new int[64];
            newBoard = MoveGen.MakeMoveCopy(board, move[0], move[1]);
            
            if (opposition.Contains(move[1]))
            {
                //newScore += values[newBoard[move[1]]];
            }
            double newPos = PosVal(newBoard, move[1]);

            score += (newPos - oldPos);

            return score;
        }


        public static double[][] minimax(int[] board, int[] player, int max_level, double alpha = -9999999, double beta = 999999999, int level = 0, double? currentBoardVal = null)
        {
            double[] bestMove = new double[2];

            if (level == max_level)
            {
                MoveEval.count += 1;
                double[] boardVal = new double[1] { (double)currentBoardVal };
                double[][] output = { null, boardVal};
                return output;
            }

            if (currentBoardVal is null)
                currentBoardVal = BoardVal(board, player);

            double bestScore;
            if (level % 2 == 0)
                bestScore = -999999;
            else
                bestScore = 9999999;

            foreach (int[] move in MoveGen.AllMoves(board, player))
            {
                double newBoardVal = SmartBoardVal(board, player, (double)currentBoardVal, move);
                int[] newBoard = MoveGen.MakeMoveCopy(board, move[0], move[1]);

                int[] opposition = new int[6];
                if (Board.white == player)
                    opposition = Board.black;
                else
                    opposition = Board.white;

                double[] score = minimax(newBoard, opposition, max_level, alpha, beta, level + 1, currentBoardVal = newBoardVal)[1];
                if (level % 2 == 0)
                {
                    if (score[0] > bestScore)
                    {
                        bestScore = (double)score[0];
                        bestMove[0] = (double)move[0];
                        bestMove[1] = (double)move[1];
                        alpha = Math.Max(alpha, bestScore);
                        if (alpha >= beta)
                            break;
                    }
                }
                else
                {
                    if (score[0] < bestScore)
                    {
                        bestScore = (double)score[0];
                        bestMove[0] = (double)move[0];
                        bestMove[1] = (double)move[1];
                        beta= Math.Min(beta, bestScore);
                        if (alpha >= beta)
                            break;
                    }
                }
            }

            double[] highScore = new double[1];
            highScore[0] = Convert.ToInt32(bestScore);
            double[][] moveChosen = { bestMove, highScore };
            return moveChosen;

 
        }

        /*
        public static int[] Minimax(int[] board, int[] player, int max_level, int alpha = -9999999, int beta = 9999999, int level = 0, double currentBoardVal = 1.2345)
        {

            if (level == max_level)
            {
                count += 1;
                test
            }
        }


        */



    }
}
