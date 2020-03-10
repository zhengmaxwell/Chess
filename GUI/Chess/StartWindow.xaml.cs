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
using System.Windows.Shapes;

namespace Chess
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
    public partial class StartWindow : Window
    {
        public StartWindow()
        {
            InitializeComponent();
        }

        private void PVP_Click(object sender, RoutedEventArgs e)
        {
            GameWindow game = new GameWindow();
            game.AI = false;
            game.Show();
            this.Close();
        }

        private void PvAI_Click(object sender, RoutedEventArgs e)
        {
            GameWindow game = new GameWindow();
            game.AI = true;
            game.Show();
            this.Close();
        }
    }
}
