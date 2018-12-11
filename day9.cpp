#include<iostream>
#include<vector>
#include<list>

using namespace std;

int main() {

  // variables
  size_t num_players = 431;
  size_t last_marble_worth = 70950*100;

  //num_players = 10;
  //last_marble_worth = 1618;

  vector<unsigned long> players(num_players, 0);
  list<unsigned long> circle;
  //circle.reserve(last_marble_worth);
  circle.push_back(0);
  circle.push_back(2);
  circle.push_back(1);

  //size_t current_marble_index = 1;
  unsigned long next_marble_number = 3;
  unsigned long last_score = 0;
  size_t turn = 3;

  std::list<unsigned long>::iterator it = circle.begin();
  it++;

  while (next_marble_number < last_marble_worth) {
    if (next_marble_number%23 == 0) {
      //const size_t remove_idx = (circle.size()+current_marble_index-7)%circle.size();
      std::list<unsigned long>::iterator remove_it = it;
      for (size_t i=7; i>0; i--) {
        if (remove_it == circle.begin())
          remove_it = circle.end();
        --remove_it;
      }
      //const unsigned long remove_val = circle[remove_idx];
      const unsigned long remove_val = *remove_it;
      //circle.erase(circle.begin()+remove_idx);
      it = circle.erase(remove_it);
      if (it == circle.end())
        it = circle.begin();
      //current_marble_index = remove_idx;
      last_score = next_marble_number + remove_val;

      size_t player = turn%num_players;
      players[player] += last_score;
    } else {
      //current_marble_index = (current_marble_index+2)%circle.size();
      for (size_t i=2; i>0; i--) {
        if (it == circle.end())
          it = circle.begin();
        it++;
      }
      //if (current_marble_index == 0) {
      //  current_marble_index = circle.size();
        //circle.push_back(next_marble_number);
      //} else {
        //it = circle.insert(circle.begin()+current_marble_index, next_marble_number);
      //}
      it = circle.insert(it,next_marble_number);
    }

    turn++;
    next_marble_number++;

    if (turn%10000 == 0) {
      //std::cout<<"Turn: "<<turn<<", cur_idx="<<current_marble_index<<", next_num="<<next_marble_number<<std::endl;
      std::cout<<"Turn: "<<turn<<", next_num="<<next_marble_number<<std::endl;
    }
  }

  unsigned long high_score = 0;
  size_t winner_idx = 0;
  for (size_t i = 0; i < players.size(); i++) {
    //std::cout<<"Player "<<i+1<<": "<<players[i]<<std::endl;
    if (players[i] > high_score) {
      high_score = players[i];
      winner_idx = i;
    }
  }
  std::cout<<"Winner is player "<<winner_idx+1<<" with "<<players[winner_idx]<<" points."<<std::endl;

  return 0;
}
