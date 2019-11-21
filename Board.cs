using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;



namespace Chess
{

    public static class Board
    {
        public static int[] pawn = new int[2]   { 10, 20 };
        public static int[] knight = new int[2] { 11, 21 };
        public static int[] bishop = new int[2] { 12, 22 };
        public static int[] rook = new int[2]   { 13, 23 };
        public static int[] queen = new int[2]  { 14, 24 };
        public static int[] king = new int[2]   { 15, 25 };

        static public int[] white = new int[6] { 10, 11, 12, 13, 14, 15 };
        public static int[] black = new int[6] { 20, 21, 22, 23, 24, 25 };

        public static int[] game = Default();
        public static int[] test = TestBoard();

        public static Dictionary<int, string> pieces = new Dictionary<int, string>()
        {
            {00 , " " },
            {20 , "♟"},
            {21 , "♞"},
            {22 , "♝"},
            {23 , "♜"},
            {24 , "♛"},
            {25 , "♚"},
            {10 , "♙"},
            {11 , "♘"},
            {12 , "♗"},
            {13 , "♖"},
            {14 , "♕"},
            {15 , "♔"},
            {99 , "★" }
        };
        
        public static int[] GetRowCol(int pos)
        {
            int[] output = new int[2] { pos / 8, pos % 8 };
            return output;
        }

        public static int GetPos(int row, int col)
        {
            return row * 8 + col;
        }

        public static int[] Default()
        {
            int[] board = new int[64]  {13, 11, 12, 14, 15, 12, 11, 13,
                                        10, 10, 10, 10, 10, 10, 10, 10,
                                        00, 00, 00, 00, 00, 00, 00, 00,
                                        00, 00, 00, 00, 00, 00, 00, 00,
                                        00, 00, 00, 00, 00, 00, 00, 00,
                                        00, 00, 00, 00, 00, 00, 00, 00,
                                        20, 20, 20, 20, 20, 20, 20, 20,
                                        23, 21, 22, 24, 25, 22, 21, 23};
            return board;
        }

        public static int[] TestBoard()
        {
            int[] board = new int[64]  {00, 00, 00, 00, 00, 00, 00, 00,
                                        10, 00, 00, 00, 00, 00, 00, 00,
                                        00, 00, 00, 00, 00, 00, 00, 00,
                                        00, 00, 00, 00, 00, 00, 00, 00,
                                        00, 00, 00, 00, 00, 00, 00, 00,
                                        00, 00, 00, 00, 00, 00, 00, 00,
                                        00, 00, 00, 20, 00, 00, 00, 00,
                                        23, 21, 22, 24, 25, 22, 21, 23};
            return board;
        }
    }



}