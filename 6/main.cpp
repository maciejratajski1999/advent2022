#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <fstream>
std::string readFile(std::string filename){
    std::fstream file;
    file.open(filename, std::ios_base::in);
    std::string text;
    std::string temp;
    while (std::getline(file, temp)) text = text + temp;
    file.close();
    return text;
}
std::set<char> toSet(std::vector<char> v)
{
    std::set<char> s(v.begin(), v.end());
    return s;
}
int findSequence(std::string input, int length=4){
    std::vector<char> tempSequence;
    int position = 0;
    for (char c : input){
        ++position;
        tempSequence.push_back(c);
        if (tempSequence.size() == length){
            if (tempSequence.size() == toSet(tempSequence).size()) return position;
            else tempSequence.erase(tempSequence.begin());
        }
    }
    return NULL;
}

int main() {
//    std::string inputString = "bvsvcsssfwwdttzpzqqnjjmbbmpbmpmffnttjllzbblvlvqllcwwqpwwhcclqqhmhbhlbbmtmdmgmpggcmcnmcmfcfddvmmcncrcncbbtssdnnhmmfmfrmrbbzllgtllfnnwhwtwzwjjrsrgsrsbbnjjbhjbbjpplslrssdwswrrcsszpplpfplflnnvdvmvjmmgpghphlhphnhffgqgfgzgddstdsdjjgqglqggtgvgrrgtrtllrvrmmnggftgtdtrttgqttcrcqqjqcqwccdzdldrdbbbmrbbnmmwrmmbcchnhmhchddhpphdhzhbbnvbbtctwcwbcwcfclcwwzvwvddbsdsfftgtqggjllwjwppmvvswsjwsscdcrrbggqzqqbhhjwhjwjtjvttpnpdplljplpqpzqzrqrmqmvvsvrvppfgfzfqffvsfvfcvcddjcddzssgfgtffhtfhthntnvvzhzwhzhbbnvvbtbqtqcqnqwnnvpvwwcqcgqqwrwlwbwrbbjcbbqqpddtbddcldccddjssvnvlnnmggmbbchcdcqqdsdqsdqdvdpvvvbzvbvrrjdrjrbjbrbttqzttmffwcfcnnbjnbbjmmgtmgmgdgdpgdglgzzvnzzztjjwbwvvhbhwbbnbhbddwcwvcvjcvjjnnjqjqjzqjjbgbmbjjnqnqddgfgwfgwfftntvnvtvhvlvslsffhvvwnnhshchmmlwmmwvvnhnggzllphllbqqtgqqffhwwnwzztnzttftptnppdpjdjwdwhdddgqglqldqdzzslsggstsrrcsrcclqqrsqrqjqhhjwjggrjgjnjtjwtwjtjrrvnnbddzqzzfnnbvvmfvmvwvggmsgsrggcjjtftpfflzfzccdgcgzcgzcggrbgbngnpnfngfnfqqfzfbfsbfsslqsstvvfmvfvrrvdrddrlrjlrrngrrgfgvgdggnttqqjbjwbwwchhddpmmcvcppjttbzbrzrdzztgtrrchhhbnnqfnfjnnpncnbnvnfnwwsllvrvddhwdwndnjdjbjttmggfvggjhghrhggczgzttbnttjmmdhdrrnnmppwtwdtdbtdbdffpqplqqfbffjssllmwmnmffcnczzrnznzmmwcmwwpbpcbbfdfrrznnzwnnmjnngmngmgpgrppnhnjhhjnhjhfhbffcfhccvzccnrrsggtjtdtjjqqdmqqcggmzzrhzrrbnnlqqtlqtqhhcffrpffgcfgcgncgnggjgzgvzvtztctmtgmmfwwttrntrtqtptzpzjpjqjffpvffvdfvvjhhggfhfrhrwhhwshsnhshbbjzbjzzlvlfvffmrfffngfgpglgjjsbbvzzjsjvsslgsgsfggwjgjlgjgsjgsstvstvstsffdqdpqddrsrmmjbbqbffzbzjjvzvrvcvhhsjsrrmccgqqjnnplnnrprhppslsqszzpvzvggsqscqqbwqqccsdsswqswwqcqzqddbhhmggswggzllccwvwjjpqqrpplrprgrllfwfmwmhhcmmnppfffvtffndnsdnsnbsnsgnsncnzzwrrqrwwzhzbzbnbqbjjrhhjjjbcjjffmwffjnfjfbbjtbbjhjvhvshvhwvwhvwvwfwwwfvvlddqnnlttqssnpsprpwwttlwtwrwfflggvjggwswgwgtgccdjdtdldrdcdsspjpvjpvvfttjrjdrrjppddbdvdjdwdvdssrhsszsjzzfccmwcwzzlnljlppjdjsdjdhdttrdtdtvddslsmmjnmmhzmhhmwmvmcvclvlnndtdrrfdrfrvfvsfvsszfsfdsfdsfsnsdsnsbsddsdwwzbbfqqhrhmrmzmhzhbbpptptffvtvhhwqqtgtdthhrqrrvttprtprrbcblsmbwqqpffmwnqmrdwvjszzhhhffpqsphcgqhlmsgnmmjsdhbfjscztgfvhnlbcmccrfcbnrwcpvgzztvpjdplmncrbvpzwtdnpfwcpvcbzvbtpqmgztsblnchzlphtzgfqcwnrbpcdhbcgzsbgdmbhhrsjqcngfddwvwvldbftgccbjzrrqjcnhbdfgmpdhdgfqzmnpmjgtgwvqlbwgjzjppgmcjzrfzgnbjjbvmshllzjppscwjzjqnbvrppzlshfvtvnpwljrghhwdhfgtcrstnqtqdzfhvgbrrzfdwgtjpjccwrphsdrsjlrlbnrtdbnhpdtshmqlpjqjdlwvrrflwqhcmnsrmcdnfcnwwqmdjlqmqvpgggrjrvfwtwnmhrgzztvmnqczvgmvpcldgfwmtmnsvdshrjmtsgfstjllmqqmpttfhjnsjflcmnpqtqnvtpbgjjhlwqzmrgrbvcsjvprbtqdrnvrgfjdrlhdjsvhhzvllzgfbdwbtqbqzpllpcmcdrfmrsfnwvvmhcqjblnczltcmmmbqwpztqmdpprwphfwgwnsvnzsldnvbsbcdprnztpbmlfzcwpdvcwbsdflrcvsqlswctvlpvshqpwvtcjbtfnmgwtgsvtqhqdzzfhwznggpsmsmzlzrzqcdbqcnhpwhjbhvnqrcwnvpspwqmsqhdbchgrfcmznchwvftgvbldnvtpgmthbmpvccqwbjnjpzhrstscncsrdzsptzvlzjwnpzshmzbhrhgmnwmjmzvvvbgdjshgnqcmdmjrnhqzwtzpjvdczqzccvpvpqnftvpcwgzrzmmnhjnphfntbgjnscwqjcgfcrhjdsjbqfgzhsftghwwwvjwmhfhbwrwmnfrhcggcrjtjsqndrgsbvddqtwhctltzswmtsgwjgsbvvsvzfhbptjqbvbblzhcmnpcjpgzfhstsnlfvmqbdjhszhwhbqztvfdhnbnmppwvzjpnrhtbgthrdprjpqwpthqwzdnhpngflcmhnrmsbdlfwhjbfgrhfzspmfvvtqrwldzvblbtlwqfgfflvmvthbvdzzbtmmpzchgmldmgnhrfhhjwstbqqrzhmqsbqhjzdmjmllmjgqhhjghgsvrbmrbfjdzghmwpszfmslfwcjrftbqjgbbzddtvjmsgwmhhdzwtwvrgqctvwbwjqvssdvfprjsdgsgwbfmzwzmbnlzbfdqvwbrzpgvngqhfqzfqqsvmtgvsqwrplhfnsqhtvtbbqmpbjlcsfjgngwrztlrjbmcjddjsnbgcpnhdtngzhzvhzpjfcblhglhzfsjdgjdqvvppfrdftfbfldwqjznvrdqdnfscgvhztjwlqgqbjmlsbcrldjhnrsfgthlhplvwgmdnplrtpdvrqbpvnbpzfzwlvrrscvmgzhlcdwglwwrgzqsjqsqfblqljltbvvjwbpmfqjvldspgsbjrdbbwzjntlpqgvdjfvsjznczsppzwfvblffqqhwmhzdzztbvbsjhvjtjrptrdvrbbpnpncltqnhdvwjgzcmdtnbnhlmptjsqlzlpztnrtclgsmgvrvggtzfhpwgjgwtrnshmcpvhprpnrvgprspmwhchlhhsvwpvjdmjrlnjdchngrdgpwzsgqsjnqnqwsctzvsmqgvrpffffcfshbhmqbffwvcjqscrwhbfflwslspwjgdbvcgbtwldzffrdhrlbssjbcsjgbhprgspnjdbmnshzqwdvtnzsrfwbqfrgnlmpvqrrmmmcshzltqbwffprbwqbfthtvszqzcbbljtfjqmwpqssjtdpqlrfmpchrqmdpbsdjcdmglnlgnwvhclqfmbwhtljmscnzzqtwtjqsqrmmnssmqhqjvdlpmstmpwmrcfjbjrchrgvqqzbvtzpcbdvchvghnflllqddlttjwtnfhgqjjgtgsnhpvnwhcbljstshmhpwbqthvngqzrmqpmwqnvrfblpjlqgczfmtwvmlbzslqwdzhfccmrvjwfnwzgpbvgdgttdgtjdlvrmpbdhwjsvvsjqpclrnbtzphvmpfqhhqdmbmqzwphnzzfqjsqvdvbvnpmtnzpdsfzmbttssnssrtpmpvgrrzvcljtqtrqnfmmtsnvtrsjgcmqnttcmp";
    std::string inputString = readFile("input.txt");
    int startOfPacketPosition = findSequence(inputString);
    std::cout << startOfPacketPosition << std::endl;

    int startOfMessagePosition = findSequence(inputString, 14);
    std::cout << startOfMessagePosition << std::endl;
    return 0;
}
