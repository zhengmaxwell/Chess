using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Threading;

namespace Chess
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class GameWindow : Window
    {
        public bool AI; // 0 - PvP; 1 - PvAI;
        public int difficulty = 2;
        protected int turn = 0; // white starts
        protected int click = 0;
        protected int oldPos;
        protected int oldVal;
        protected int newPos;
        protected int[] board = Board.game;
        protected int[] white = Board.white;
        protected int[] black = Board.black;

        

        public GameWindow()
        {
            
            InitializeComponent();

            PrintBoard(Buttons(), board);
        }


        public IEnumerable<Button> Buttons()
        {
             IEnumerable<Button> buttons = ChessBoard.Children.OfType<Button>();

            return buttons;
        }


        public void PrintBoard(IEnumerable<Button> buttons, int[] board, int pos = -1, int AI_oldPos = -1, int AI_newPos = -1)
        {
            
            foreach (Button btn in buttons)
            {
                btn.Content = Board.pieces[board[ChessBoard.Children.IndexOf(btn)]];
                btn.FontSize = 40;

                if((ChessBoard.Children.IndexOf(btn) + ChessBoard.Children.IndexOf(btn) / 8) % 2 == 0)
                {
                    btn.Background = Brushes.BurlyWood;
                }
                else
                {
                    btn.Background = Brushes.Brown;
                }

                if (pos != -1)
                {
                    if (board[pos] != 0)
                    {
                        if (MoveGen.GetMoves(board, pos).Contains(ChessBoard.Children.IndexOf(btn)))
                        {
                            btn.Background = Brushes.ForestGreen;
                        }
                    }
                }

                if (AI_oldPos != -1 && AI_newPos != -1)
                {
                    int[] AI_move = new int[2] { AI_oldPos, AI_newPos };
                    if (AI_move.Contains(ChessBoard.Children.IndexOf(btn)))
                    {
                        btn.Background = Brushes.Yellow;
                    }
                }
            }
        }


        private void BtnClick(object sender, RoutedEventArgs e)
        {
            int pos = ChessBoard.Children.IndexOf((e.Source as Button));

            int[] player;

            if (turn % 2 == 0)
            {
                player = white;
            }
            else
            {
                player = black;
            }

            if (click == 0) // first click
            {
                if (player.Contains(board[pos]))
                {
                    PrintBoard(Buttons(), board, pos);
                    oldPos = pos;
                    oldVal = board[pos];
                    click = 1;
                }
            }
            else // second click
            {
                if (pos == oldPos)
                {
                    PrintBoard(Buttons(), board);
                    click = 0;
                }
                else if (player.Contains(board[pos]))
                {
                    PrintBoard(Buttons(), board, pos);
                    oldPos = pos;
                    oldVal = board[pos];
                    click = 1;
                }
                else
                {
                    if (MoveGen.GetMoves(board, oldPos).Contains(pos))
                    {
                        board[oldPos] = 0;
                        board[pos] = oldVal;
                        PrintBoard(Buttons(), board);
                        click = 0;
                        turn += 1;
                        if (AI) //PvAI
                        {
                            player = black;
                            oldPos = (int)MoveEval.minimax(board, player, difficulty)[0][0];
                            newPos = (int)MoveEval.minimax(board, player, difficulty)[0][1];
                            board = MoveGen.MakeMove(board, oldPos, newPos);
                            //Thread.Sleep(1000);
                            PrintBoard(Buttons(), board, AI_oldPos: oldPos, AI_newPos: newPos);
                            turn += 1;
                        }
                    }
                    else
                    {
                        PrintBoard(Buttons(), board);
                        click = 0;
                    }
                }
            }
        }
    }

    public class PVP : GameWindow
    {
        
    }

    
}
